# create_db.py

from app.models.base import Base
from app.database import engine  # jahan aapka engine create hua hai

def create_database():
    print("Creating database and tables...")
    Base.metadata.create_all(bind=engine)
    print("Database and tables created successfully!")

if __name__ == "__main__":
    create_database()
