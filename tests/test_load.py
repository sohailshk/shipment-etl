import pytest
import pandas as pd
import os
from src.load import load

def test_load_creates_csvs(tmp_path):
    df = pd.DataFrame({
        "tracking_number": ["A", "B"],
        "payment_type": ["COD", "PREPAID"],
        "pickup_datetime_ist": ["2020-01-01T10:00:00+05:30", "2020-01-02T10:00:00+05:30"],
        "delivery_datetime_ist": ["2020-01-02T10:00:00+05:30", "2020-01-03T10:00:00+05:30"],
        "days_taken": [1, 1],
        "shipment_weight_kg": [1, 2],
        "pickup_pincode": ["111", "222"],
        "pickup_city": ["A", "B"],
        "pickup_state": ["S", "T"],
        "drop_pincode": ["333", "444"],
        "drop_city": ["C", "D"],
        "drop_state": ["U", "V"],
        "delivery_attempts": [2, 3]
    })
    detail_out = tmp_path / "detail.csv"
    summary_out = tmp_path / "summary.csv"
    load(df, str(detail_out), str(summary_out))
    # Check files exist
    assert detail_out.exists()
    assert summary_out.exists()
    # Check columns
    detail = pd.read_csv(detail_out)
    summary = pd.read_csv(summary_out)
    assert set(detail.columns) == set(df.columns)
    assert set(summary.columns) == {"days_mean", "days_median", "days_mode", "att_mean", "att_median", "att_mode"}
    # Check values
    assert summary["days_mean"].iloc[0] == 1
    assert summary["att_mode"].iloc[0] == 2 or summary["att_mode"].iloc[0] == 3
