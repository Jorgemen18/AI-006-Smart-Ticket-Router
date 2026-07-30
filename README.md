# 🎫 AI-006 Smart Ticket Router

Un enrutador inteligente de tickets de soporte técnico con enfoque Enterprise, desarrollado con **FastAPI**, **Azure OpenAI** y **Docker**.

La API funciona como el primer nivel de atención al cliente. Recibe quejas o solicitudes de soporte, analiza el sentimiento del mensaje mediante Inteligencia Artificial, clasifica automáticamente el tipo de incidencia, asigna una prioridad utilizando reglas de negocio y genera una respuesta profesional estructurada para agilizar el proceso de atención.

---

# 🚀 Arquitectura del Sistema

El proyecto combina Inteligencia Artificial Generativa con reglas de negocio tradicionales para reducir alucinaciones, mejorar la consistencia de las respuestas y garantizar un correcto escalamiento de los tickets.

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
Reglas de Negocio
   │
   ▼
Respuesta JSON
```

---

# 🛠️ Tecnologías Utilizadas

- Python 3.10+
- FastAPI
- Pydantic
- Azure OpenAI (GPT)
- Docker
- Docker Compose

### Próximamente

- GitHub Actions (CI/CD)
- Azure Container Apps
- Azure Monitor
- Application Insights

---

# 📌 Características

- Análisis automático de sentimiento.
- Clasificación inteligente de tickets.
- Priorización basada en reglas de negocio.
- Asignación automática del equipo responsable.
- Generación de respuestas profesionales mediante IA.
- API REST documentada con Swagger.
- Contenedorización completa con Docker.
- Preparado para despliegue en Azure.

---

# 📂 Estructura del Proyecto

```text
AI-006-Smart-Ticket-Router
│
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── prompts/
│   ├── utils/
│   └── main.py
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🔗 Enlaces

**Repositorio**

```
https://github.com/TU_USUARIO/AI-006-Smart-Ticket-Router
```

**Producción**

```
Próximamente
```

**Swagger**

```
http://localhost:8000/docs
```

**OpenAPI**

```
http://localhost:8000/openapi.json
```

**Métricas**

```
http://localhost:8000/api/v1/metrics
```

---

# 🐳 Ejecución Local con Docker

Este proyecto está diseñado siguiendo la filosofía **Docker First**, por lo que únicamente necesitas tener instalado Docker Desktop.

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/AI-006-Smart-Ticket-Router.git

cd AI-006-Smart-Ticket-Router
```

---

## 2. Configurar variables de entorno

Crear un archivo llamado `.env` en la raíz del proyecto.

```env
AZURE_OPENAI_ENDPOINT=tu_endpoint

AZURE_OPENAI_API_KEY=tu_api_key

AZURE_OPENAI_DEPLOYMENT_NAME=tu_modelo

AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

## 3. Construir la imagen

```bash
docker compose build
```

---

## 4. Levantar los contenedores

```bash
docker compose up
```

o bien

```bash
docker compose up --build
```

La aplicación estará disponible en:

```
http://localhost:8000
```

---

# 📡 API Endpoints

## Analizar Ticket

**POST**

```
/api/v1/tickets/analyze
```

### Request

```json
{
  "text": "¡Es el colmo! Me volvieron a cobrar doble la mensualidad en mi tarjeta. Si no me regresan mi dinero hoy mismo, voy a llamar a mi abogado.",
  "language": "es"
}
```

### Response

```json
{
  "category": "Facturación",
  "priority": "Crítica",
  "sentiment": "Muy Negativo",
  "recommended_team": "Retención y Finanzas",
  "suggested_response": "Lamentamos profundamente el error en su facturación. Hemos escalado su caso con prioridad crítica para procesar su reembolso inmediato.",
  "estimated_sla": "2 horas"
}
```

---

## Dashboard de Métricas

**GET**

```
/api/v1/metrics
```

### Response

```json
{
  "tickets_processed": 142,
  "high_priority": 23,
  "billing": 45,
  "technical": 80,
  "sales": 12,
  "other": 5
}
```

---

# 📈 Flujo del Procesamiento

1. El cliente envía un ticket.
2. FastAPI recibe la solicitud.
3. Pydantic valida la información.
4. Azure OpenAI analiza el contenido.
5. Se identifica el sentimiento.
6. Se clasifica la categoría.
7. Se calcula la prioridad.
8. Se determina el equipo responsable.
9. Se genera una respuesta profesional.
10. La API devuelve un JSON estructurado.

---

# 📸 Capturas de Pantalla

Pendiente de agregar:

- Swagger UI
- Docker Desktop
- Logs del contenedor
- Ejemplos de peticiones
- Dashboard de métricas

---

# 📅 Roadmap

- [x] Configuración inicial del proyecto.
- [x] API con FastAPI.
- [x] Integración con Azure OpenAI.
- [x] Dockerización del proyecto.
- [ ] Pruebas unitarias.
- [ ] GitHub Actions.
- [ ] Azure Container Apps.
- [ ] Azure Monitor.
- [ ] Application Insights.
- [ ] Autenticación con Azure Entra ID.

---

# 👨‍💻 Autor

**Jorge**

Proyecto desarrollado como parte de mi portafolio de Ingeniería en Inteligencia Artificial y preparación para la certificación **Microsoft Azure AI Engineer Associate (AI-103)**.