from pydantic import BaseModel

class TicketResponse(BaseModel):
    category: str
    priority: str
    sentiment: str
    recommended_team: str
    suggested_response: str
    estimated_sla: str