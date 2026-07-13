"""Centralized logger — writes to logs/automation.log and stdout."""
import logging
import os
from datetime import datetime

from utils.config_reader import CONFIG

_LOG_DIR = CONFIG["paths"]["logs"]
os.makedirs(_LOG_DIR, exist_ok=True)

_LOG_FILE = os.path.join(_LOG_DIR, f"automation_{datetime.now().strftime('%Y%m%d')}.log")

_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=_FORMAT,
    handlers=[
        logging.FileHandler(_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def get_logger(name: str) -> logging.Logger:
    """Return a namespaced logger."""
    return logging.getLogger(name)
