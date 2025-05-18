from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router
from app.db.session import engine, Base
from contextlib import asynccontextmanager
from app.db.session import SessionLocal
from app.db.seeds import seed_categories, seed_admin_users
from app.core.config import settings

def create_tables():
    """
    Create database tables if they do not exist.
    """

    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    db = SessionLocal()
    try:
        # Seed the database with initial data
        seed_admin_users(db)
        seed_categories(db)
    finally:
        db.close()

    yield  # This is where FastAPI runs

def create_app():
    """
    Create and configure the FastAPI application.
    """
    app = FastAPI(
        title=settings.APPLICATION_NAME,
        description=settings.APPLICATION_DESCRIPTION,
        version=settings.APPLICATION_VERSION,
        lifespan=lifespan,
    )

    # Configure CORS
    origins = [
        "http://localhost:3000",
        "https://your-frontend-domain.com",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include the API router
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Create database tables
    create_tables()

    return app

app = create_app()