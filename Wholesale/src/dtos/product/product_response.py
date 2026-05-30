from datetime import datetime
from pydantic import BaseModel, Field

class ProductResponseDTO(BaseModel):
    id: int
    barcode: str
    name: str
    description: str
    brand: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    active: bool
    created_at: datetime
    updated_at: datetime
