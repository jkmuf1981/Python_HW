# conftest.py
import os
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Student

# Строка подключения
DB_URI = os.getenv("DATABASE_URL", "postgresql://postgres:secret@localhost:5432/hw_database")

# Инициализация движка и сессии
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

# Общая фикстура для сессии
@pytest.fixture(scope="session")
def db_session():
    session = Session()
    yield session
    session.close()

# Автотест очищает базу данных после каждого теста
@pytest.fixture(autouse=True)
def reset_db(db_session):
    db_session.query(Student).delete()
    db_session.commit()