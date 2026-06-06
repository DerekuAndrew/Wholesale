from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from config.database import get_db
from dtos.product.product_create import ProductCreateDTO
from dtos.product.product_response import ProductResponseDTO
from dtos.product.product_update import ProductUpdateDTO
from services.product_service import ProductService

# Router de productos
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Endpoints del CRUD
@router.get("/", response_model=List[ProductResponseDTO], status_code=status.HTTP_200_OK)
def get_products(db: Session = Depends(get_db)):
    return ProductService.get_products(db = db)

@router.get("/{product_id}", response_model=ProductResponseDTO, status_code=status.HTTP_200_OK)
def find_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.find_product(product_id = product_id, db = db)

@router.post("/", response_model=ProductResponseDTO, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreateDTO, db: Session = Depends(get_db)):
    return ProductService.create_product(dto = data, db = db)

@router.put("/", response_model=ProductResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_product(data: ProductUpdateDTO, db: Session = Depends(get_db)):
    return ProductService.update_product(dto = data, db = db)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ProductService.delete_product(product_id = product_id, db = db)
