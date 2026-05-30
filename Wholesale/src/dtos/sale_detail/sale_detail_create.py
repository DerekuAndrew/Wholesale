from pydantic import BaseModel, Field

class SaleDetailCreateDTO(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
