from fastapi import FastAPI
from app.routers import auth, users, reminders, motivation, notifications
from app.routers.tracking import router as tracking_router  # Correct import for tracking router
from app.utils.config import settings
from app.database import engine
from app.models import base
from dotenv import load_dotenv
import os
from app.models.base import Base
from app.database import engine
import app.models

load_dotenv()  # .env file load karta hai

SECRET_KEY = os.getenv("SECRET_KEY")
print("SECRET_KEY:", settings.SECRET_KEY)  # Debugging ke liye, baad me hata sakte ho

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App", version="1.0.0")

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(reminders.router)
app.include_router(motivation.router)
app.include_router(notifications.router)
app.include_router(tracking_router)  # Use imported router here

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Backend!"}
