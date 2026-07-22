# UD01 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar el desarrollo de la **Unidad Didáctica 1 (Desarrollo Profesional en Python para IA)**, debes verificar y preparar el software y la infraestructura necesarios en tu entorno de trabajo.

---

## 🛠️ Requisitos de Software

### 1. Intérprete de Python
- **Versión requerida:** Python 3.11 o superior.
- **Verificación en consola:**
  ```bash
  python --version
  ```
  *(Debe mostrar Python 3.11.x o superior).*

### 2. Gestor de Proyectos `uv` (Astral)
- **Instalación:**
  - **Linux / macOS:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  - **Windows (PowerShell):**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
- **Verificación en consola:**
  ```bash
  uv --version
  ```

### 3. Control de Versiones con Git
- **Verificación de instalación:**
  ```bash
  git --version
  ```
- **Configuración inicial de usuario:**
  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu_correo@centro.edu"
  ```

### 4. Entorno de Desarrollo (VS Code)
Se recomienda **Visual Studio Code** con las siguientes extensiones instaladas:
- **Python** (`ms-python.python`)
- **Pylance** (`ms-python.vscode-pylance`)
- **Ruff** (`charliermarsh.ruff`) - Linter y formateador de código.
- **Marp for VS Code** (`marp-team.marp-vscode`) - Para visualizar y exportar las diapositivas de la unidad.

---

## 💻 Requisitos de Hardware y Red

- **Memoria RAM:** Mínimo 4 GB.
- **Almacenamiento:** 1 GB de espacio libre en disco.
- **Conectividad:** Acceso a la red local del centro educativo para la sincronización con el servidor Git interno (GitLab / Gitea).

---

## 🚀 Verificación del Entorno
Ejecuta los siguientes comandos desde tu terminal dentro de una carpeta vacía para comprobar que tu entorno está listo:

```bash
uv init test_env
cd test_env
uv add pydantic pytest
uv run pytest
```
Si la ejecución finaliza sin errores, tu equipo está listo para iniciar la **UD01**.
