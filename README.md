# 🎫 AI-006 Smart Ticket Router

> Intelligent Enterprise Support Ticket Routing API powered by **FastAPI**, **Azure OpenAI**, **Docker** and **Azure Container Apps**.

## 📖 Descripción

AI-006 Smart Ticket Router es una API REST que funciona como el primer nivel de atención al cliente.

La aplicación recibe el texto de una solicitud o queja, utiliza **Azure OpenAI** para analizar el contenido y posteriormente aplica reglas de negocio para generar una respuesta estructurada que incluye:

- Análisis de sentimiento.
- Clasificación automática del ticket.
- Priorización del caso.
- Equipo responsable recomendado.
- Tiempo estimado de atención (SLA).
- Respuesta profesional sugerida.

Este proyecto fue desarrollado como parte de mi portafolio de **Azure AI** utilizando una arquitectura moderna basada en contenedores y desplegada completamente en Microsoft Azure.

---

# 🌐 Demo en Producción

### Swagger UI

https://aca-smart-ticket-router.lemontree-8658bace.southcentralus.azurecontainerapps.io/docs

### OpenAPI

https://aca-smart-ticket-router.lemontree-8658bace.southcentralus.azurecontainerapps.io/openapi.json

---

# 🚀 Arquitectura

```text
Cliente
   │
   ▼
FastAPI
   │
   ▼
Validación (Pydantic)
   │
   ▼
Azure OpenAI
   │
   ▼
Business Rules Engine
   │
   ▼
Respuesta JSON
```

---

# 🛠 Tecnologías Utilizadas

## Backend

- Python 3.10
- FastAPI
- Pydantic

## Inteligencia Artificial

- Azure OpenAI
- GPT
- Prompt Engineering

## Contenedores

- Docker
- Docker Compose

## Cloud

- Azure Container Registry (ACR)
- Azure Container Apps

## DevOps

- GitHub
- GitHub Actions

---

# ✨ Características

- Análisis automático de sentimiento.
- Clasificación inteligente de tickets.
- Priorización basada en reglas de negocio.
- Asignación automática del equipo responsable.
- Generación de respuestas utilizando Azure OpenAI.
- API REST documentada con Swagger.
- Contenedorización completa con Docker.
- Despliegue automático mediante GitHub Actions.
- Aplicación pública ejecutándose en Azure Container Apps.

---

# 📂 Estructura del Proyecto

```text
AI-006-Smart-Ticket-Router
│
├── backend/
│   ├── models/
│   ├── services/
│   ├── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔗 Enlaces

## Repositorio

https://github.com/Jorgemen18/AI-006-Smart-Ticket-Router

## API Pública

https://aca-smart-ticket-router.lemontree-8658bace.southcentralus.azurecontainerapps.io

## Swagger

https://aca-smart-ticket-router.lemontree-8658bace.southcentralus.azurecontainerapps.io/docs

---

# 🐳 Ejecución Local

## Clonar el repositorio

```bash
git clone https://github.com/Jorgemen18/AI-006-Smart-Ticket-Router.git

cd AI-006-Smart-Ticket-Router
```

---

## Variables de entorno

Crear un archivo `.env`

```env
AZURE_OPENAI_ENDPOINT=

AZURE_OPENAI_API_KEY=

AZURE_OPENAI_DEPLOYMENT_NAME=

AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

## Construir el contenedor

```bash
docker compose build
```

---

## Ejecutar

```bash
docker compose up
```

La API quedará disponible en

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# 📡 Endpoints

## POST

```
/api/v1/tickets/analyze
```

### Request

```json
{
    "text":"Mi laptop se quedó sin batería y el cargador está roto.",
    "language":"es"
}
```

### Response

```json
{
    "category":"Soporte Técnico",
    "priority":"Media",
    "sentiment":"Negativo",
    "recommended_team":"Equipo de Soporte Técnico",
    "suggested_response":"...",
    "estimated_sla":"6 horas"
}
```

---

# 📈 Flujo del Procesamiento

1. El cliente envía un ticket.
2. FastAPI recibe la solicitud.
3. Pydantic valida los datos.
4. Azure OpenAI analiza el contenido.
5. Se determina el sentimiento.
6. Se identifica la categoría.
7. Se aplican reglas de negocio.
8. Se calcula la prioridad.
9. Se asigna el equipo responsable.
10. Se genera la respuesta estructurada.

---

# ☁️ Despliegue en Microsoft Azure

## Azure Container Registry (ACR)

La imagen Docker se almacena en un registro privado de Azure para administrar las versiones de la aplicación.

📸<img width="789" height="428" alt="Captura de pantalla 2026-07-30 155214" src="https://github.com/user-attachments/assets/386f5796-f5f3-4936-a992-cd877a34587c" />


---

## GitHub Actions

Cada cambio enviado a la rama **main** ejecuta automáticamente un pipeline que:

- Construye la imagen Docker.
- Publica la imagen en Azure Container Registry.
- Actualiza Azure Container Apps.

📸 <img width="910" height="490" alt="Captura de pantalla 2026-07-30 155703" src="https://github.com/user-attachments/assets/2cf57e89-1d9c-494a-b818-95d8cbcd4a8d" />


---

## Azure Container Apps

La aplicación se ejecuta como un servicio Serverless utilizando Azure Container Apps.

Características del despliegue:

- Imagen almacenada en Azure Container Registry.
- Variables de entorno administradas desde Azure.
- Integración con Azure OpenAI.
- Exposición pública mediante HTTPS.
- Escalado administrado por Azure.

📸 <img width="937" height="679" alt="Captura de pantalla 2026-07-30 162452" src="https://github.com/user-attachments/assets/3de61083-4c42-40fe-8923-0090682b59c6" />


---

# 🎉 Resultado

La aplicación se encuentra completamente desplegada en Microsoft Azure y puede probarse desde cualquier navegador mediante Swagger.

🌐 **Swagger**

https://aca-smart-ticket-router.lemontree-8658bace.southcentralus.azurecontainerapps.io/docs

📸 <img width="925" height="989" alt="Captura de pantalla 2026-07-30 162626" src="https://github.com/user-attachments/assets/e26dea1a-b661-4943-b016-0c80a0ecad9f" />

---

# 📸 <img width="903" height="933" alt="Captura de pantalla 2026-07-30 162651" src="https://github.com/user-attachments/assets/d2c40485-df74-42b9-8e86-9f57a601543d" />


- Arquitectura del proyecto.
- Swagger UI.
- Docker Desktop.
- Azure Container Registry.
- Azure Container Apps.
- GitHub Actions.
- Respuesta exitosa de la API.

---

# 📅 Roadmap

- ✅ API REST con FastAPI.
- ✅ Integración con Azure OpenAI.
- ✅ Docker.
- ✅ Docker Compose.
- ✅ Azure Container Registry.
- ✅ GitHub Actions.
- ✅ Azure Container Apps.


---

# 👨‍💻 Autor

**Jorge**

Proyecto desarrollado como parte de mi portafolio de **Azure AI** y preparación para la certificación **Microsoft Azure AI Engineer Associate (AI-103)**.

Si este proyecto te resulta interesante, cualquier comentario o sugerencia es bienvenido.
