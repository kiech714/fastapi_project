from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgresql://fastapi_db_hfiw_user:GytQ6ghlrRU6iOMNJeQYq6KUdN9Ktps0@dpg-d0itovre5dus739vaccg-a.frankfurt-postgres.render.com/fastapi_db_hfiw


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
