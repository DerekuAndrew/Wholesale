from datetime import datetime
from dtos.sale.sale_response import SaleResponseDTO
from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO

sales_data: SaleResponseDTO = [
    SaleResponseDTO(
        id=1,
        folio="SALE-0001",
        location_id=1,
        datetime=datetime.fromisoformat("2026-05-21T19:10:55+00:00"),
        total=99.00,
        status="CREATED",
        created_at=datetime.fromisoformat("2026-05-21T19:10:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T19:10:55+00:00"),
        details=[
            SaleDetailResponseDTO(
                id=1,
                sale_id=1,
                product_id=1,
                quantity=2,
                unit_price=28.50,
                subtotal=57.00
            ),
            SaleDetailResponseDTO(
                id=2,
                sale_id=1,
                product_id=2,
                quantity=1,
                unit_price=42.00,
                subtotal=42.00
            )
        ]
    )
]
