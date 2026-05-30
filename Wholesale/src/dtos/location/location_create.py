from pydantic import BaseModel, Field, EmailStr

class LocationCreateDTO(BaseModel):
    client_id: int
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr