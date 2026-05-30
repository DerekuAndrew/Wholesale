from datetime import datetime
from dtos.product.product_response import ProductResponseDTO

products_data: ProductResponseDTO = [
    ProductResponseDTO(
        id=1,
        barcode="7501000111111",
        name="Arroz blanco 1 kg",
        description="Bolsa de arroz blanco de grano largo",
        brand="Campo Real",
        price=28.50,
        stock=120,
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    ),
    ProductResponseDTO(
        id=2,
        barcode="7501000222222",
        name="Aceite vegetal 1 L",
        description="Botella de aceite vegetal para cocina",
        brand="La Cocina",
        price=42.00,
        stock=80,
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    ),
    ProductResponseDTO(
        id=3,
        barcode="7501000333333",
        name="Frijol pinto 1 kg",
        description="Bolsa de frijol pinto seleccionado",
        brand="Campo Real",
        price=36.75,
        stock=95,
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    )
]
