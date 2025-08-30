from fastapi import FastAPI
from .routers import router
from .config.logging_config import setup_logging
from .config.settings import settings

# Setup logging base on environment
setup_logging(settings.ENVIRONMENT)

app = FastAPI(
    title=settings.API_TITLE, 
    description=settings.API_DESCRIPTION
)

app.include_router(router)