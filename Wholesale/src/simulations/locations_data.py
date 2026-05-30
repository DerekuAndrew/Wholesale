from datetime import datetime
from dtos.location.location_response import LocationResponseDTO

locations_data: LocationResponseDTO = [
    LocationResponseDTO(
        id=1,
        client_id=1,
        name='Walmart Tijuana 2000',
        address='Corredor Tijuana - Rosarito 2000 No. 819, Pob Delejido Francisco Villa',
        city='Tijuana',
        state='Baja California',
        postal_code='22236',
        phone='6642118659',
        email='walmart2000@email.mx',
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    ),
    LocationResponseDTO(
        id=2,
        client_id=1,
        name='Walmart Macroplaza',
        address='Av de los Insurgentes 18015, Rio Tijuana 3ra Etapa',
        city='Tijuana',
        state='Baja California',
        postal_code='22226',
        phone='8009256278',
        email='walmart_macroplaza@email.mx',
        active=True,
        created_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00"),
        updated_at=datetime.fromisoformat("2026-05-21T18:45:55+00:00")
    )
]