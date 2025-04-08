import os
import logging
from enum import Enum
from logging.handlers import RotatingFileHandler

class LoggingLvl(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

def setup_app_logging(
    log_dir: str ="logs",
    log_file: str ="ft-api.log",
    max_bytes: int = 1_000_000,
    backup_count: int = 3,
    file_level: str = "DEBUG",
    console_level: str = "INFO"
):
    def resolve_log_level(level):
        if isinstance(level, str):
            try:
                return LoggingLvl[level.upper()].value
            except KeyError:
                raise ValueError(f"Invalid logging level: {level}")
        return level
    
    file_level = resolve_log_level(file_level)
    console_level = resolve_log_level(console_level)

    log_path = os.path.join(log_dir, log_file)
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(file_level)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(console_level)
    logger.addHandler(console_handler)

    logger.debug("Logging has been configured.")
