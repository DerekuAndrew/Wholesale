from dotenv import load_dotenv
import os

# Cargamos las variables de entorno
load_dotenv()

class Settings:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION", "no")

    if DB_TRUSTED_CONNECTION.lower() == "yes":
        DATABASE_URL = (
            f"mssql+pyodbc://@"
            f"{DB_SERVER}/"
            f"{DB_DATABASE}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&trusted_connection=yes"
            "&TrustServerCertificate=yes"
        )
    else:
        DATABASE_URL = (
            f"mssql+pyodbc://"
            f"{DB_USERNAME}:"
            f"{DB_PASSWORD}@"
            f"{DB_SERVER}/"
            f"{DB_DATABASE}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&TrustServerCertificate=yes"
        )

settings = Settings()
