from app.core.config import settings
from pymongo import MongoClient
import psycopg2

def get_database():
    """Returns the appropriate database connection based on DB_TYPE."""
    if settings.DB_TYPE == "mongodb":
        if not settings.MONGO_URI:
            raise ValueError("MONGO_URI must be set for MongoDB")
        client = MongoClient(settings.MONGO_URI)
        return client.get_database()

    elif settings.DB_TYPE == "postgres":
        if not settings.POSTGRES_URI:
            raise ValueError("POSTGRES_URI must be set for PostgreSQL")
        return psycopg2.connect(settings.POSTGRES_URI)

    else:
        raise ValueError(f"Unsupported DB_TYPE: {settings.DB_TYPE}")
