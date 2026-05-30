from typing import List
from fastapi import APIRouter
from starlette import status
from dtos.sale.sale_create import SaleCreateDTO
from dtos.sale.sale_response import SaleResponseDTO
from dtos.sale.sale_update import SaleUpdateDTO
from services.sale_service import SaleService

# Router de ventas
router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

# Endpoints del CRUD
@router.get("/", response_model=List[SaleResponseDTO], status_code=status.HTTP_200_OK)
def get_sales():
    return SaleService.get_sales()

@router.get("/{sale_id}", response_model=SaleResponseDTO, status_code=status.HTTP_200_OK)
def find_sale(sale_id: int):
    return SaleService.find_sale(sale_id=sale_id)

@router.post("/", response_model=SaleResponseDTO, status_code=status.HTTP_201_CREATED)
def create_sale(data: SaleCreateDTO):
    return SaleService.create_sale(dto=data)

@router.put("/", response_model=SaleResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_sale(data: SaleUpdateDTO):
    return SaleService.update_sale(dto=data)

@router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: int):
    SaleService.delete_sale(sale_id=sale_id)
