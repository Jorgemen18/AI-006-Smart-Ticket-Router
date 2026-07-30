import os
from openai import AzureOpenAI
import json

# Inicializamos el cliente leyendo las variables de entorno inyectadas por Docker
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

def classify_and_route_ticket(ticket_text: str) -> dict:
    """
    Envía el ticket a Azure OpenAI y le pide que devuelva un JSON estructurado
    con la clasificación, sentimiento, prioridad y sugerencia de respuesta.
    """
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    # Prompt del sistema (Reglas de negocio estrictas)
    system_prompt = """
    Eres un enrutador inteligente de tickets de soporte nivel Senior.
    Tu trabajo es leer la queja del cliente y devolver ÚNICAMENTE un objeto JSON válido.
    
    Reglas de negocio para la Prioridad:
    - Si el sentimiento es 'Muy Negativo' y la categoría es 'Facturación', la prioridad es 'Crítica'.
    - Si el cliente menciona 'demanda', 'abogado' o 'cancelar', la prioridad es 'Alta'.
    
    El JSON debe tener exactamente esta estructura:
    {
        "category": "Facturación | Soporte Técnico | Ventas | Otro",
        "priority": "Baja | Media | Alta | Crítica",
        "sentiment": "Positivo | Neutral | Negativo | Muy Negativo",
        "recommended_team": "Nombre del equipo sugerido",
        "suggested_response": "Un borrador de respuesta profesional para el cliente",
        "estimated_sla": "Tiempo estimado de resolución (ej. 2 horas)"
    }
    """
    
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": ticket_text}
        ],
        response_format={ "type": "json_object" }, # Obligamos a que responda en JSON
        temperature=0.0 # Temperatura 0 para que sea analítico y no creativo
    )
    
    # Extraemos el texto de la respuesta y lo convertimos a un diccionario de Python
    result_text = response.choices[0].message.content
    return json.loads(result_text)