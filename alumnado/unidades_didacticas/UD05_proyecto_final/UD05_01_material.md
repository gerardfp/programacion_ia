# UD05 - Guía del Proyecto Final para el Alumnado

## 🎯 Caso Empresarial: Integración de IA en una Empresa Cerámica (Sur de Castellón)

Como proyecto final del módulo se plantea la integración de capacidades de inteligencia artificial generativa en la aplicación web existente de una **empresa ficticia de fabricación y comercialización de pavimentos y revestimientos cerámicos del clúster industrial del sur de Castellón** (Onda, Vila-real, l'Alcora).

> [!NOTE]
> **Delimitación del Andamiaje Provisto:**  
> La aplicación base suministra la infraestructura convencional necesaria (interfaz web, autenticación de usuarios, catálogo, base de datos relacional con `pgvector`, imágenes, fichas técnicas y **plantillas de pruebas unitarias parcialmente preparadas**).  
> Los endpoints de CRM y pedidos forman parte del andamiaje proporcionado y **no constituyen contenidos nuevos del proyecto**. Tu trabajo se concentra en la integración de las capacidades de IA y sus mecanismos de control mediante el **AI Harness**.

---

## 🏗️ Los 3 Subsistemas a Desarrollar

```text
┌────────────────────────────────────────────────────────────────────────┐
│             APLICACIÓN WEB EMPRESA CERÁMICA (CASTELLÓN)                │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌────────────────┐ │
│   │ 1. Asistente        │  │ 2. Visualizador     │  │ 3. Asistente   │ │
│   │    Catálogo y RAG   │  │    de Ambientes     │  │    Comercial   │ │
│   │ • Fichas técnicas   │  │ • Foto de estancia  │  │    y Pedidos   │ │
│   │ • Usos y formatos   │  │ • Selección azulejo │  │ • Extracción   │ │
│   │ • Citas técnicas    │  │ • Renderizado       │  │ • Validación   │ │
│   │ • Consulta de stock │  │   multimodal guiado │  │ • Confirmación │ │
│   └─────────────────────┘  └─────────────────────┘  └────────────────┘ │
│              │                        │                      │         │
└──────────────┼────────────────────────┼──────────────────────┼─────────┘
               ▼                        ▼                      ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        AI HARNESS DEL ALUMNO                           │
│  Contratos Pydantic • Control de Acceso • Reglas de Pedido • Auditoría │
└────────────────────────────────────────────────────────────────────────┘
```

### 1. Asistente Comercial y Catálogo Técnico (RAG + Tools de Consulta)
La aplicación incorpora un asistente conversacional capaz de responder preguntas sobre las especificaciones de los productos cerámicos (pavimentos exteriores vs interiores, acabados y recomendaciones de colocación).

**Requisitos de Ingeniería:**
- Las respuestas deben respaldarse en la información recuperada, con citas explícitas a la ficha técnica como mecanismo de verificación y apoyo.
- El sistema debe emitir abstención formal ("NO_DATA") ante consultas sobre productos no documentados.
- El asistente puede invocar herramientas de consulta para complementar la respuesta: `consultar_producto(codigo)` y `consultar_stock(referencia)`.

---

### 2. Visualizador de Ambientes (Integración Multimodal Guiada)
La aplicación permite al usuario cargar una fotografía de una estancia real (salón, cocina o terraza) y seleccionar un producto del catálogo cerámico (ej. azulejo imitación madera o gres porcelánico).

Mediante un servicio de IA multimodal o generativo de imágenes preconfigurado por la aplicación, el sistema genera una representación visual del espacio integrando el producto cerámico seleccionado.

**Objetivo de Aprendizaje:** No programas un modelo de difusión desde cero; **integras una capacidad multimodal existente dentro de una aplicación web mediante contratos de API claros**, gestionando la transferencia de imágenes, los parámetros del servicio y el control de errores o latencias. El objetivo evaluable se centra estrictamente en interpretar y gestionar el contrato de la API de integración (parámetros, latencia, respuestas tipadas y manejo de errores), no en la calidad estética o artística del renderizado generado.

---

### 3. Asistente Comercial, CRM y Gestión de Pedidos Simulados
El asistente acompaña al cliente en la selección y formalización de su compra bajo el axioma central:
> **El LLM interpreta; la aplicación calcula.**

1. El LLM identifica preferencias del cliente y extrae los $m^2$ solicitados. Actualiza el CRM simulado (`POST /api/crm/contacts`).
2. **Cálculo exacto por la aplicación:** El modelo no realiza operaciones matemáticas ni determina importes económicos por sí mismo. Invoca una herramienta determinista (`calcular_cajas(producto, m2)`) que aplica fórmulas exactas y reglas de precio oficial de la empresa.
3. Prepara el resumen del borrador del pedido simulado (`POST /api/orders/simulate`).
4. **Flujo de confirmación con consecuencias:**
   ```text
   LLM extrae m² y producto solicitado
         ↓
   Tool determinista: calcular_cajas(producto, m2) y calcular_precio(...)
         ↓
   Validación sintáctica (Pydantic: campos requeridos y tipos)
         ↓
   Reglas de negocio (Harness: comprobación de stock y pedido mínimo de cajas)
         ↓
   Autorización (Harness: verificación de permisos del usuario)
         ↓
   Presentación del resumen e importe calculado al usuario
         ↓
   Confirmación explícita (Human-in-the-Loop en la interfaz web)
         ↓
   Registro de pedido simulado (POST /api/orders/confirm) + Auditoría en log
   ```
   Se aplica el principio rector: **a mayor impacto de una acción, mayor nivel de control requerido**. Las acciones críticas (formalizar compras o registrar pedidos) exigen confirmación humana y registro de auditoría, impidiendo que el LLM ejecute acciones de forma autónoma.

---

## 📊 Matriz de Transferencia: De las Prácticas al Proyecto

| Lo que aprendiste en las Prácticas Independientes (40 h) | Cómo lo aplicas en la Empresa Cerámica (10 h) |
|---|---|
| **Structured Output** | Extraer preferencias del cliente, metros cuadrados y datos de contacto desde el diálogo. |
| **Pydantic** | Validar rigurosamente los argumentos de pedidos y los datos del CRM antes de procesarlos. |
| **RAG** | Asistente de catálogo técnico (especificaciones y usos de pavimentos y revestimientos). |
| **Embeddings** | Búsqueda semántica de colecciones cerámicas por descripción de estilo o acabado. |
| **Control de Acceso (ACL)** | Filtrado en base de datos para evitar que documentación restringida llegue al contexto. |
| **Tool Calling** | Consultar stock en almacén, verificar referencias y preparar borradores de pedido. |
| **Reglas de Negocio** | Verificar stock disponible y condiciones mínimas de pedido de la empresa. |
| **Autorización** | Controlar qué usuarios tienen permiso para registrar pedidos en firme. |
| **Confirmación de Acciones** | Exigir confirmación explícita del cliente antes de registrar el pedido simulado. |
| **Persistencia** | Almacenamiento en PostgreSQL de clientes, contactos y pedidos simulados. |
| **Multimodalidad** | Visualizador de ambientes: envío de imagen de estancia + producto cerámico para renderizado. |
| **Evaluación Operacional** | Comprobar respuestas del catálogo sobre el dataset cerrado de 20 casos cerámicos. |
| **Seguridad (Prompt Injection)** | Impedir que instrucciones del usuario modifiquen valores económicos calculados o eludan la confirmación. |
| **Auditoría Básica** | Registrar en log cada pedido simulado, usuario responsable e importe confirmado. |

---

## 📋 Entregables del Proyecto

1. **Código Fuente del AI Harness:** Repositorio Git limpio con archivo de bloqueo `uv.lock`, variables de entorno en `.env.example` y sin credenciales en el código.
2. **Suite de Pruebas Unitarias:** Tests con `pytest` que validen los esquemas Pydantic, las reglas de negocio y las consultas SQL parametrizadas.
3. **Reporte de Evaluación del Catálogo:** Ejecución del script de evaluación sobre el dataset de 20 casos de prueba midiendo *Hit Rate @ k* y comprobando el respaldo de respuestas y citas en las fuentes.
4. **Defensa Técnica Oral (10 min):** Presentación individual (2 min) y respuesta a 3 preguntas aleatorias del banco docente sobre las decisiones de diseño arquitectónico y la gestión de fallos.
