from pydantic import BaseModel, Field

class ProductCreateDTO(BaseModel):
    barcode: str
    name: str
    description: str
    brand: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
