from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List
from dtos.location.location_response import LocationResponseDTO

class ClientResponseDTO(BaseModel):
    id:int
    name: str
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr
    rfc: str = Field(min_length=12, max_length=12)
    active: bool
    created_at: datetime
    updated_at: datetime

    locations: List[LocationResponseDTO] = []
    class Config:
        from_attributes = True