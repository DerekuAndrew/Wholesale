from pydantic import BaseModel, Field, EmailStr

class ClientCreateDTO(BaseModel):
    name: str
    phone: str = Field(min_length=10, max_length=10)
    email: EmailStr
    rfc: str = Field(min_length=12, max_length=12)