"""
load.py
Write detail and summary CSVs.
"""
import pandas as pd
from .utils import log_and_print

def load(df: pd.DataFrame, detail_out: str, summary_out: str) -> None:
    """Write detail and summary CSVs."""
    log_and_print(f"Starting load(detail_out={detail_out}, summary_out={summary_out})", "info")
    try:
        df.to_csv(detail_out, index=False)
        log_and_print(f"Detail CSV written to {detail_out}", "info")
        summary = pd.DataFrame({
            "days_mean":   [df.days_taken.mean()],
            "days_median": [df.days_taken.median()],
            "days_mode":   [df.days_taken.mode().iat[0] if not df.days_taken.mode().empty else None],
            "att_mean":    [df.delivery_attempts.mean()],
            "att_median":  [df.delivery_attempts.median()],
            "att_mode":    [df.delivery_attempts.mode().iat[0] if not df.delivery_attempts.mode().empty else None],
        })
        summary.to_csv(summary_out, index=False)
        log_and_print(f"Summary CSV written to {summary_out}", "info")
    except Exception as e:
        log_and_print(f"load() failed: {e}", "error")
        raise
