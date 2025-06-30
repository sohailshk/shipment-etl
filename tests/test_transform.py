import pytest
import pandas as pd
from src.transform import transform

def test_transform_days_taken():
    # 24h apart
    data = [{
        "trackDetails": [{
            "trackingNumber": "X",
            "specialHandlings": [],
            "shipmentWeight": {"value": 1},
            "shipperAddress": {"city": "A", "stateOrProvinceCode": "S", "postalCode": "111"},
            "destinationAddress": {"city": "B", "stateOrProvinceCode": "T", "postalCode": "222"},
            "datesOrTimes": [
                {"type": "ACTUAL_PICKUP", "dateOrTimestamp": "2020-01-01T10:00:00+05:30"},
                {"type": "ACTUAL_DELIVERY", "dateOrTimestamp": "2020-01-02T10:00:00+05:30"}
            ],
            "events": []
        }]
    }]
    df = transform(data)
    assert df["days_taken"].iloc[0] == 1

def test_transform_delivery_attempts():
    # 2 OD, 1 DL
    data = [{
        "trackDetails": [{
            "trackingNumber": "Y",
            "specialHandlings": [],
            "shipmentWeight": {"value": 1},
            "shipperAddress": {"city": "A", "stateOrProvinceCode": "S", "postalCode": "111"},
            "destinationAddress": {"city": "B", "stateOrProvinceCode": "T", "postalCode": "222"},
            "datesOrTimes": [
                {"type": "ACTUAL_PICKUP", "dateOrTimestamp": "2020-01-01T10:00:00+05:30"},
                {"type": "ACTUAL_DELIVERY", "dateOrTimestamp": "2020-01-02T10:00:00+05:30"}
            ],
            "events": [
                {"eventType": "OD"},
                {"eventType": "OD"},
                {"eventType": "DL"}
            ]
        }]
    }]
    df = transform(data)
    assert df["delivery_attempts"].iloc[0] == 3

def test_transform_columns():
    # Check columns
    data = [{
        "trackDetails": [{
            "trackingNumber": "Z",
            "specialHandlings": [],
            "shipmentWeight": {"value": 1},
            "shipperAddress": {"city": "A", "stateOrProvinceCode": "S", "postalCode": "111"},
            "destinationAddress": {"city": "B", "stateOrProvinceCode": "T", "postalCode": "222"},
            "datesOrTimes": [
                {"type": "ACTUAL_PICKUP", "dateOrTimestamp": "2020-01-01T10:00:00+05:30"},
                {"type": "ACTUAL_DELIVERY", "dateOrTimestamp": "2020-01-02T10:00:00+05:30"}
            ],
            "events": []
        }]
    }]
    df = transform(data)
    expected = [
        "tracking_number", "payment_type", "pickup_datetime_ist", "delivery_datetime_ist", "days_taken", "shipment_weight_kg", "pickup_pincode", "pickup_city", "pickup_state", "drop_pincode", "drop_city", "drop_state", "out_for_delivery_datetimes", "delivery_attempts"
    ]
    assert list(df.columns) == expected

def test_transform_out_for_delivery_datetimes():
    # Test for unique, sorted OD datetimes in IST, no duplicates
    data = [{
        "trackDetails": [{
            "trackingNumber": "W",
            "specialHandlings": [],
            "shipmentWeight": {"value": 1},
            "shipperAddress": {"city": "A", "stateOrProvinceCode": "S", "postalCode": "111"},
            "destinationAddress": {"city": "B", "stateOrProvinceCode": "T", "postalCode": "222"},
            "datesOrTimes": [
                {"type": "ACTUAL_PICKUP", "dateOrTimestamp": "2020-01-01T10:00:00+05:30"},
                {"type": "ACTUAL_DELIVERY", "dateOrTimestamp": "2020-01-02T10:00:00+05:30"}
            ],
            "events": [
                {"eventType": "OD", "timestamp": {"$numberLong": "1577865600000"}},
                {"eventType": "OD", "timestamp": {"$numberLong": "1577865600000"}},  # duplicate
                {"eventType": "OD", "timestamp": {"$numberLong": "1577952000000"}}
            ]
        }]
    }]
    df = transform(data)
    od_col = df["out_for_delivery_datetimes"].iloc[0]
    od_list = od_col.split(";") if od_col else []
    assert len(od_list) == 2  # Only two unique datetimes
    assert od_list == sorted(od_list)
    # Check IST format (should not contain +05:30 or UTC offset)
    for dt in od_list:
        assert "+" not in dt and "UTC" not in dt
