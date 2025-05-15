from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Twój connection string z Rendera (upewnij się, że go nie trzymasz publicznie w produkcji)
DATABASE_URL = "postgresql://fastapi_db_hfiw_user:GytQ6ghlrRU6iOMNJeQYq6KUdN9Ktps0@dpg-d0itovre5dus739vaccg-a.frankfurt-postgres.render.com/fastapi_db_hfiw"

# Tworzenie silnika bazy danych
engine = create_engine(DATABASE_URL)

# Utworzenie sesji i bazy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Funkcja zależności do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
