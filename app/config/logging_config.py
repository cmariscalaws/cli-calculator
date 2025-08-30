import logging
import logging.config
import os
from pathlib import Path
from datetime import datetime

"""
    Custom formatter that includes microseconds.
"""
class MirosecondFormatter(logging.Formatter):
    """
        Override formatTime to include microseconds.
    """
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = datetime(*ct[:6]).strftime(datefmt)
            # Add microseconds
            s += f".{int(record.msecs):06d}"
            return s
        else:
            t = datetime(*ct[:6])
            return t.strftime('%Y-%m-%d %H:%M:%S.%f')

"""
Get logging configuration based on environment.
"""
def get_logging_config(environments: str = "development") -> dict:
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    if environments == "production":
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'detailed': {
                    '()': MirosecondFormatter, # Use custom formatter
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                },
                'simple': {
                    'format': '%(levelname)s - %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'WARNING',
                    'formatter': 'simple'
                },
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': log_dir / 'app.log',
                    'maxBytes': 10485760, # 10MB
                    'backupCount': 5,
                    'level': 'INFO',
                    'formatter': 'detailed'
                },
                'error_file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': log_dir / 'error.log',
                    'maxBytes': 10485760, # 10MB
                    'backupCount': 5,
                    'level': 'ERROR',
                    'formatter': 'detailed'
                }
            },
            'loggers': {
                'app': {
                    'handlers': ['console', 'file', 'error_file'],
                    'level': 'INFO',
                    'propogate': False
                }
            },
            'root': {
                'handlers': ['console', 'file'],
                'level': 'WARNING'
            }
        }
    else: # development
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'detailed': {
                    '()': MirosecondFormatter, # Use custom formatter
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                },
                'colored': {
                    '()': MirosecondFormatter, # Use custom formatter
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'colored'
                },
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': log_dir / 'app.log',
                    'maxBytes': 10485760, # 10MB
                    'level': 'DEBUG',
                    'formatter': 'detailed'
                }
            },
            'loggers': {
                'app': {
                    'handlers': ['console', 'file'],
                    'level': 'DEBUG',
                    'propogate': False
                }
            },
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG'
            }
        }

"""
    Setup logging configuration.
"""
def setup_logging(environment: str = None):
    if environment is None:
        environment = os.getenv('ENVIRONMENT', 'development')
    
    config = get_logging_config(environment)
    logging.config.dictConfig(config)

    #Get logger for this module
    logger = logging.getLogger(__name__)
    
    # Use print for setup message to avoid formatter issues
    print(f"Logging configured for {environment} environment")

    return logger