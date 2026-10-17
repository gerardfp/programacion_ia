#!/usr/bin/env bash
set -Eeuo pipefail

# ============================================================
# Configuración
# ============================================================

VM="agente-a"
IMAGE="24.04"

CPU=2
RAM="2G"
DISK="10G"

AGENT_LOCAL="./dangerous_tool_calling.py"

PROJECT_DIR="/home/ubuntu"
AGENT_REMOTE="$PROJECT_DIR/dangerous_tool_calling.py"
MARKER="$PROJECT_DIR/.agente-a-prepared"

OLLAMA_PORT=11434

# Modos de ejecución
RECONFIGURE=0
RESET=0

# ============================================================
# Argumentos
# ============================================================

mostrar_ayuda() {
    cat <<'EOF'
Uso: ./ejecutar_en_vm.sh [opción]

Opciones:
  --reconfigure  Reinstala los requisitos y configura el proyecto,
                 conservando la VM y sus archivos.
  --reset        Destruye la VM y la crea de nuevo desde cero.
  -h, --help     Muestra esta ayuda.

Sin opciones, prepara la VM solo si es necesario y ejecuta el agente.
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --reconfigure)
            RECONFIGURE=1
            ;;
        --reset)
            RESET=1
            ;;
        -h|--help)
            mostrar_ayuda
            exit 0
            ;;
        *)
            echo "ERROR: Opción desconocida: $1" >&2
            mostrar_ayuda
            exit 1
            ;;
    esac
    shift
done

if [[ "$RECONFIGURE" -eq 1 && "$RESET" -eq 1 ]]; then
    echo "ERROR: --reconfigure y --reset son incompatibles." >&2
    exit 1
fi

# ============================================================
# Funciones auxiliares
# ============================================================

info() {
    echo
    echo "==> $*"
}

error() {
    echo "ERROR: $*" >&2
    exit 1
}

vm_existe() {
    multipass info "$VM" >/dev/null 2>&1
}

# ============================================================
# 1. Comprobar requisitos del anfitrión
# ============================================================

# Asegurarse manualmente de multipass usa el driver qemu
# multipass stop --all
# multipass set local.driver=qemu


command -v multipass >/dev/null 2>&1 ||
    error "Multipass no está instalado."

multipass version >/dev/null 2>&1 ||
    error "No se puede acceder a Multipass."

[[ -f "$AGENT_LOCAL" ]] ||
    error "No se encuentra $AGENT_LOCAL."

# ============================================================
# 2. Reset opcional
# ============================================================

if [[ "$RESET" -eq 1 ]] && vm_existe; then
    info "Destruyendo la VM existente"

    multipass delete --purge "$VM"
fi

# ============================================================
# 3. Crear la VM si no existe
# ============================================================

if ! vm_existe; then
    info "Creando VM Ubuntu $IMAGE"

    multipass launch "$IMAGE" \
        --name "$VM" \
        --cpus "$CPU" \
        --memory "$RAM" \
        --disk "$DISK"
else
    echo "La VM '$VM' ya existe."
fi

# ============================================================
# 4. Arrancar la VM si está detenida
# ============================================================

STATE=$(multipass info "$VM" |
    awk '/^State:/ {print $2; exit}')

if [[ "$STATE" != "Running" ]]; then
    info "Arrancando la VM"
    multipass start "$VM"
fi

# ============================================================
# 5. Esperar a que la VM esté operativa
# ============================================================

info "Esperando a que la VM responda"

READY=0

for _ in $(seq 1 60); do
    if multipass exec "$VM" -- true >/dev/null 2>&1; then
        READY=1
        break
    fi

    sleep 2
done

[[ "$READY" -eq 1 ]] ||
    error "La VM no ha respondido a tiempo."

# ============================================================
# 6. Comprobar si hay que preparar el entorno
# ============================================================

NEEDS_SETUP=0

if [[ "$RECONFIGURE" -eq 1 ]]; then
    NEEDS_SETUP=1
elif ! multipass exec "$VM" -- env PROJECT_DIR="$PROJECT_DIR" \
    bash -lc '
        test -f "$PROJECT_DIR/.agente-a-prepared" &&
        test -x "$HOME/.local/bin/uv" &&
        test -f "$PROJECT_DIR/pyproject.toml"
    ' >/dev/null 2>&1; then
    NEEDS_SETUP=1
fi

# ============================================================
# 7. Preparar el entorno solo cuando sea necesario
# ============================================================

if [[ "$NEEDS_SETUP" -eq 1 ]]; then

    info "Instalando requisitos del sistema"

    multipass exec "$VM" -- bash -lc '
        set -e

        sudo apt-get update

        sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
            python3 \
            ca-certificates \
            curl

        sudo apt-get clean
        sudo rm -rf /var/lib/apt/lists/*
    '

    # --------------------------------------------------------
    # Instalar uv si no está disponible
    # --------------------------------------------------------

    info "Comprobando uv"

    multipass exec "$VM" -- bash -lc '
        set -e

        if [[ ! -x "$HOME/.local/bin/uv" ]]; then
            curl -LsSf https://astral.sh/uv/install.sh | sh
        fi

        "$HOME/.local/bin/uv" --version
    '

    # --------------------------------------------------------
    # Crear la configuración del proyecto
    # --------------------------------------------------------

    info "Configurando el proyecto Python"

    multipass exec "$VM" -- env PROJECT_DIR="$PROJECT_DIR" \
        bash -lc '
            set -e

            mkdir -p "$PROJECT_DIR"

            cat > "$PROJECT_DIR/pyproject.toml" << "EOF"
[project]
name = "agente-a"
version = "0.1.0"
description = "Agente experimental para ejecutar tareas en Linux"
requires-python = ">=3.10"
dependencies = [
    "httpx>=0.27,<1",
]
EOF
        '

else
    info "El entorno ya está preparado; se conserva."
fi

# ============================================================
# 8. Copiar el agente actualizado
# ============================================================

info "Copiando dangerous_tool_calling.py"

multipass transfer \
    "$AGENT_LOCAL" \
    "$VM:$AGENT_REMOTE"

# ============================================================
# 9. Instalar dependencias si se está preparando
# ============================================================

if [[ "$NEEDS_SETUP" -eq 1 ]]; then

    info "Instalando las dependencias Python"

    multipass exec "$VM" -- env PROJECT_DIR="$PROJECT_DIR" \
        bash -lc '
            set -e

            "$HOME/.local/bin/uv" sync --project "$PROJECT_DIR"

            "$HOME/.local/bin/uv" run \
                --project "$PROJECT_DIR" \
                python -c "import httpx; print(\"httpx instalado:\", httpx.__version__)"

            touch "$PROJECT_DIR/.agente-a-prepared"
        '

fi

# ============================================================
# 10. Configurar la conexión con Ollama
# ============================================================

# Se puede proporcionar OLLAMA_HOST desde el anfitrión.
# Si no se proporciona, se detecta la puerta de enlace de la VM.

if [[ -z "${OLLAMA_HOST:-}" ]]; then

    info "Detectando la dirección del anfitrión"

    HOST_IP=$(multipass exec "$VM" -- \
        ip route show default |
        awk '{print $3; exit}')

    [[ -n "$HOST_IP" ]] ||
        error "No se ha podido detectar la puerta de enlace."

    OLLAMA_HOST="http://${HOST_IP}:${OLLAMA_PORT}"
fi

# Elimina una posible barra final.
OLLAMA_HOST="${OLLAMA_HOST%/}"

echo "Servidor Ollama: $OLLAMA_HOST"

# ============================================================
# 11. Comprobar la conexión con Ollama
# ============================================================

info "Comprobando la conexión con Ollama"

if multipass exec "$VM" -- \
    curl --connect-timeout 3 --max-time 5 -fsS \
    "${OLLAMA_HOST}/api/tags" >/dev/null; then

    echo "Ollama responde correctamente."
else
    echo "AVISO: Ollama no responde desde la VM."
    echo "Comprueba la dirección de escucha y el cortafuegos."
fi

# ============================================================
# 12. Ejecutar el agente como root dentro de la VM
# ============================================================

echo
echo "============================================================"
echo " Ejecutando dangerous_tool_calling.py"
echo "============================================================"
echo
echo "VM:             $VM"
echo "Agente:         $AGENT_REMOTE"
echo "Servidor Ollama: $OLLAMA_HOST"
echo

multipass exec "$VM" -- \
    env PROJECT_DIR="$PROJECT_DIR" OLLAMA_HOST="$OLLAMA_HOST" \
    sudo --preserve-env=PROJECT_DIR,OLLAMA_HOST \
    bash -lc '
        exec /home/ubuntu/.local/bin/uv run \
            --project "$PROJECT_DIR" \
            --no-sync \
            python "$PROJECT_DIR/dangerous_tool_calling.py"
    '
