from pydantic import BaseModel, Field

class SaleDetailResponseDTO(BaseModel):
    id: int
    sale_id: int
    product_id: int
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    subtotal: float = Field(ge=0)
