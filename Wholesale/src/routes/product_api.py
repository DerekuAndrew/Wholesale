from typing import List
from fastapi import APIRouter
from starlette import status
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
def get_products():
    return ProductService.get_products()

@router.get("/{product_id}", response_model=ProductResponseDTO, status_code=status.HTTP_200_OK)
def find_product(product_id: int):
    return ProductService.find_product(product_id=product_id)

@router.post("/", response_model=ProductResponseDTO, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreateDTO):
    return ProductService.create_product(dto=data)

@router.put("/", response_model=ProductResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_product(data: ProductUpdateDTO):
    return ProductService.update_product(dto=data)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    ProductService.delete_product(product_id=product_id)
