from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routers import auth, users, reminders, motivation, notifications
from app.routers.tracking import router as tracking_router
from app.utils.config import settings
from app.database import Base, engine
import app.models
from app.settings.routers import router as settings_router

app = FastAPI()

load_dotenv()  # .env file load karta hai

SECRET_KEY = os.getenv("SECRET_KEY")
print("SECRET_KEY:", settings.SECRET_KEY)  # Debugging ke liye

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App", version="1.0.0")

origins = [
    "*"  # React frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security scheme for OAuth2 password bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token endpoint (dummy example - aap apne auth logic laga sakte ho)
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Aap yahan user validation karoge
    # For demo, har login ko dummy token return karta hu
    return {"access_token": "dummy-token-for-demo", "token_type": "bearer"}

# Protected example endpoint
@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Yahan token validation logic lagana hoga aapko
    return {"token_received": token}

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(reminders.router)
app.include_router(motivation.router)
app.include_router(notifications.router)
app.include_router(tracking_router)
app.include_router(settings_router) 

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Backend!"}

# Custom OpenAPI schema for Swagger to show Authorize button
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="API documentation with JWT auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    # Har endpoint me security requirement add karna (agar chaho)
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            # Skip the token endpoint from security requirement
            if path != "/token":
                openapi_schema["paths"][path][method]["security"] = [{"bearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
