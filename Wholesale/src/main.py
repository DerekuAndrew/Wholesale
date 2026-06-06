from fastapi import FastAPI
from routes import client_api, location_api, product_api, sale_api
import models  # Importamos los modelos para que esten disponibles

app = FastAPI(
    title="Wholesale System",
    description="API Service",
    version="1.0.0"
)

# Endpoint de entrada o de raiz
@app.get("/")
def read_root():
    return { "Hello": "World" }

# Routers de la API
app.include_router(client_api.router)
app.include_router(location_api.router)
app.include_router(product_api.router)
app.include_router(sale_api.router)
