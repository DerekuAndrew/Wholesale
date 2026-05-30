from datetime import datetime
from dtos.client.client_response import ClientResponseDTO

clients_data: ClientResponseDTO = [
    ClientResponseDTO(
        id=1,
        name='Walmart',
        phone='6647879855',
        email='walmart@email.mx',
        rfc='OED890718LF5',
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    ),
    ClientResponseDTO(
        id=2,
        name='Coppel',
        phone='6647879811',
        email='coppel@email.mx',
        rfc='YII930822ZQ5',
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    )
]