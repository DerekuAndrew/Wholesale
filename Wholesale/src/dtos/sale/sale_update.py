from typing import List
from pydantic import BaseModel, Field
from dtos.sale_detail.sale_detail_create import SaleDetailCreateDTO

class SaleUpdateDTO(BaseModel):
    id: int
    location_id: int
    status: str = "CREATED"
    details: List[SaleDetailCreateDTO] = Field(min_length=1)
