from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class ClientResponseDTO(BaseModel):
    id:int
    name: str
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr
    rfc: str = Field(min_length=12, max_length=12)
    active: bool
    created_at: datetime
    updated_at: datetime