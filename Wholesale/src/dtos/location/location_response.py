from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class LocationResponseDTO(BaseModel):
    id: int
    client_id: int
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr
    active: bool
    created_at: datetime
    updated_at: datetime