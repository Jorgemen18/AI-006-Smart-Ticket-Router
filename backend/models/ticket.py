from pydantic import BaseModel, Field

class TicketRequest(BaseModel):
    # Field(...) hace que el campo sea obligatorio.
    # Validamos que el ticket tenga al menos 10 caracteres y máximo 2000.
    text: str = Field(..., min_length=10, max_length=2000, description="Texto original escrito por el cliente")
    language: str = Field(default="es", description="Idioma en el que está escrito el ticket")