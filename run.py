import sys
from pathlib import Path

# Agregar src al path de Python
sys.path.insert(0, str(Path(__file__).parent / "Wholesale" / "src"))

# Ahora importar la app
from main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
