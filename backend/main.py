import logging
from fastapi import FastAPI, HTTPException
from backend.models.ticket import TicketRequest
from backend.models.response import TicketResponse
from backend.services.openai_service import classify_and_route_ticket

# 1. CONFIGURACIÓN DE LOGGING (Registros profesionales en consola)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Smart Ticket Router API", version="1.0")

# 2. BASE DE DATOS EN MEMORIA PARA MÉTRICAS 
# (En un proyecto real esto iría a una base de datos o sistema como Datadog/Prometheus)
metrics_db = {
    "tickets_processed": 0,
    "high_priority": 0,
    "billing": 0,
    "technical": 0,
    "sales": 0,
    "other": 0
}

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API is running inside Docker! 🐳"}

# 3. NUEVO ENDPOINT DE MÉTRICAS
@app.get("/api/v1/metrics")
def get_metrics():
    logger.info("Dashboard de métricas consultado.")
    return metrics_db

@app.post("/api/v1/tickets/analyze", response_model=TicketResponse)
def analyze_ticket(ticket: TicketRequest):
    logger.info(f"Ticket recibido. Longitud del texto: {len(ticket.text)} caracteres.")
    
    try:
        # Llamamos a la IA
        ia_result = classify_and_route_ticket(ticket.text)
        logger.info("OpenAI procesó el ticket exitosamente.")
        
        # 4. ACTUALIZAMOS LAS MÉTRICAS DE NEGOCIO
        metrics_db["tickets_processed"] += 1
        
        # Revisamos prioridad
        prioridad = ia_result.get("priority", "")
        if prioridad in ["Alta", "Crítica"]:
            metrics_db["high_priority"] += 1
            logger.warning(f"¡Alerta! Ticket de prioridad {prioridad} detectado.")
            
        # Revisamos categoría
        categoria = ia_result.get("category", "").lower()
        if "facturación" in categoria:
            metrics_db["billing"] += 1
        elif "soporte" in categoria or "técnico" in categoria:
            metrics_db["technical"] += 1
        elif "ventas" in categoria:
            metrics_db["sales"] += 1
        else:
            metrics_db["other"] += 1

        return ia_result
        
    except Exception as e:
        logger.error(f"Error procesando el ticket: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al procesar el ticket.")