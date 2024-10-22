from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from src.api.main import api_router
from src.config import settings


# Application code
app = FastAPI(
    title=settings.APP_NAME, version=settings.VERSION, description=settings.DESCRIPTION
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router)
