"""
extract.py
Read and validate shipment JSON data.
"""
import json
from .utils import log_and_print

class ExtractValidationError(Exception):
    pass

def extract(path: str) -> dict:
    """Read and validate shipment JSON from path."""
    log_and_print(f"Starting extract(path={path})", "info")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ExtractValidationError("Top-level JSON must be a list.")
        for i, record in enumerate(data):
            if "trackDetails" not in record:
                msg = f"Missing 'trackDetails' in record {i}"
                log_and_print(msg, "error")
                raise ExtractValidationError(msg)
        log_and_print(f"extract(path={path}) succeeded with {len(data)} records.", "info")
        return data
    except Exception as e:
        log_and_print(f"extract(path={path}) failed: {e}", "error")
        raise
