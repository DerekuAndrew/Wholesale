from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO

class SaleResponseDTO(BaseModel):
    id: int
    folio: str
    location_id: int
    datetime: datetime
    total: float = Field(ge=0)
    status: str
    created_at: datetime
    updated_at: datetime
    details: List[SaleDetailResponseDTO]

    class Config:
        from_attributes = True
