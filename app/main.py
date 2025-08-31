import logging
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .routers import router
from .config.logging_config import setup_logging
from .config.settings import settings

# Setup logging base on environment
setup_logging(settings.ENVIRONMENT)

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.API_TITLE, 
    description=settings.API_DESCRIPTION
)

# Add validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Convert 422 validation errors to 400 Bad Request."""
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid input data", "errors": exc.errors()}
    )


app.include_router(router)