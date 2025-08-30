import os
from pathlib import Path

class Settings:
    # Environment
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')

    # Logging
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'DEBUG' if ENVIRONMENT == 'development' else 'INFO')

    # API Settings
    API_TITLE: str = "Compound Interest Calculator"
    API_DESCRIPTION: str = "Calculate the future value of an investment or the required interest rate to reach a future value"

    # File paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    LOGS_DIR: Path = BASE_DIR / "logs"

# Global settings instance
settings = Settings()