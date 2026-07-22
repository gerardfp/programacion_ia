# UD02 - Requisitos Previos e Infraestructura de Preparación

Antes de comenzar la **Unidad Didáctica 2 (Servicios de IA Locales)**, debes verificar la disponibilidad del servidor de inferencia Ollama en la red del aula y preparar los paquetes cliente en tu equipo.

---

## 🌐 Infraestructura de Servidor y Red (Servicios de Aula)

### 1. Servidor de Inferencia Ollama
- **Dirección del Servidor:** Consulta la IP asignada por el profesorado en el aula (ejemplo: `http://192.168.1.100:11434` o `http://localhost:11434`).
- **Verificación de conexión mediante `curl`:**
  ```bash
  curl http://localhost:11434/api/tags
  ```
  *(Debe responder un JSON con la lista de modelos disponibles).*

### 2. Modelos Locales Requeridos en el Servidor
Asegúrate de que los siguientes modelos han sido descargados en el servidor:
- **`llama3.2:3b`** (Modelo por defecto para las prácticas).
- **`qwen2.5:3b`** (Para ejercicios de benchmarking).

---

## 🛠️ Requisitos de Software en el Ordenador del Alumno

### 1. Entorno Python y Dependencias
- Proyecto gestionado con `uv` (inicializado previamente en UD01).
- Librerías necesarias instalables mediante `uv add`:
  ```bash
  uv add httpx pydantic
  ```

### 2. Herramientas de Inspección HTTP
- Terminal con `curl` disponible.
- Opcional: Extensión **Thunder Client** o **Postman** en VS Code para probar manualmente las peticiones REST al servidor Ollama.

---

## 💻 Requisitos de Hardware del Alumno

- **Modo Consumidor (Recomendado):** Si utilizas el servidor Ollama del centro, cualquier ordenador cliente con **4 GB de RAM** es suficiente.
- **Modo Servidor Local (Ejecución de Ollama en el propio equipo):**
  - **Memoria RAM:** Mínimo 8 GB (16 GB recomendado).
  - **GPU (Opcional):** NVIDIA con soporte CUDA o Apple Silicon (M1/M2/M3) para mayor velocidad de inferencia.
  - **Almacenamiento:** 4 GB libres para el archivo de pesos del modelo `llama3.2:3b`.

---

## 🚀 Verificación de la Conexión a la API
Crea un script corto llamado `test_ollama.py` y ejecútalo con `uv run python test_ollama.py`:

```python
import httpx

response = httpx.get("http://localhost:11434/api/tags")
print("Modelos disponibles:", response.json())
```
Si obtienes la lista de modelos sin errores de conexión, tu entorno está listo para iniciar la **UD02**.
