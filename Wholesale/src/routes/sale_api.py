from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from config.database import get_db
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
def get_sales(db: Session = Depends(get_db)):
    return SaleService.get_sales(db = db)

@router.get("/{sale_id}", response_model=SaleResponseDTO, status_code=status.HTTP_200_OK)
def find_sale(sale_id: int, db: Session = Depends(get_db)):
    return SaleService.find_sale(sale_id = sale_id, db = db)

@router.post("/", response_model=SaleResponseDTO, status_code=status.HTTP_201_CREATED)
def create_sale(data: SaleCreateDTO, db: Session = Depends(get_db)):
    return SaleService.create_sale(dto = data, db = db)

@router.put("/", response_model=SaleResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_sale(data: SaleUpdateDTO, db: Session = Depends(get_db)):
    return SaleService.update_sale(dto = data, db = db)

@router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    SaleService.delete_sale(sale_id = sale_id, db = db)
