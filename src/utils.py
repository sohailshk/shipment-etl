"""
utils.py
Shared helpers for logging to LOG.md and console.
"""
import logging
from datetime import datetime

LOG_FILE = "LOG.md"

# Configure root logger for console
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s: %(message)s")


def log_to_md(message: str) -> None:
    """Append a timestamped message to LOG.md."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def log_and_print(message: str, level: str = "info") -> None:
    """Log to both LOG.md and console."""
    log_to_md(message)
    if level == "debug":
        logging.debug(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.info(message)
