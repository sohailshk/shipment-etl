"""
transform.py
Flatten, convert, and compute shipment metrics.
"""
import pandas as pd
from dateutil import parser
import pytz
from .utils import log_and_print

def transform(data: dict) -> pd.DataFrame:
    """Flatten and transform shipment data."""
    log_and_print("Starting transform(data)", "info")
    try:
        # Flatten all events for all trackDetails
        records = []
        for record in data:
            for td in record.get("trackDetails", []):
                tracking_number = td.get("trackingNumber")
                payment_type = None
                for sh in td.get("specialHandlings", []):
                    if sh.get("type") == "COD":
                        payment_type = "COD"
                        break
                if not payment_type:
                    payment_type = "PREPAID"
                shipment_weight_kg = td.get("shipmentWeight", {}).get("value")
                pickup_info = td.get("shipperAddress", {})
                drop_info = td.get("destinationAddress", {})
                pickup_pincode = pickup_info.get("postalCode", "")
                pickup_city = pickup_info.get("city", "")
                pickup_state = pickup_info.get("stateOrProvinceCode", "")
                drop_pincode = drop_info.get("postalCode", "")
                drop_city = drop_info.get("city", "")
                drop_state = drop_info.get("stateOrProvinceCode", "")
                # Find pickup and delivery datetimes
                pickup_dt = delivery_dt = None
                for dt in td.get("datesOrTimes", []):
                    if dt.get("type") == "ACTUAL_PICKUP":
                        pickup_dt = parser.parse(dt["dateOrTimestamp"]).astimezone(pytz.timezone("Asia/Kolkata"))
                    if dt.get("type") == "ACTUAL_DELIVERY":
                        delivery_dt = parser.parse(dt["dateOrTimestamp"]).astimezone(pytz.timezone("Asia/Kolkata"))
                # Count delivery attempts (OD + DL events)
                delivery_attempts = 0
                for ev in td.get("events", []):
                    if ev.get("eventType") in ("OD", "DL"):
                        delivery_attempts += 1
                records.append({
                    "tracking_number": tracking_number,
                    "payment_type": payment_type,
                    "pickup_datetime_ist": pickup_dt,
                    "delivery_datetime_ist": delivery_dt,
                    "days_taken": (delivery_dt - pickup_dt).days if pickup_dt and delivery_dt else None,
                    "shipment_weight_kg": shipment_weight_kg,
                    "pickup_pincode": pickup_pincode,
                    "pickup_city": pickup_city,
                    "pickup_state": pickup_state,
                    "drop_pincode": drop_pincode,
                    "drop_city": drop_city,
                    "drop_state": drop_state,
                    "delivery_attempts_count": delivery_attempts
                })
        df = pd.DataFrame(records)
        # Select and rename columns
        df = df[[
            "tracking_number",
            "payment_type",
            "pickup_datetime_ist",
            "delivery_datetime_ist",
            "days_taken",
            "shipment_weight_kg",
            "pickup_pincode",
            "pickup_city",
            "pickup_state",
            "drop_pincode",
            "drop_city",
            "drop_state",
            "delivery_attempts_count"
        ]]
        # Rename for output spec
        df = df.rename(columns={
            "delivery_attempts_count": "delivery_attempts"
        })
        # Final output columns
        df = df[[
            "tracking_number",
            "payment_type",
            "pickup_datetime_ist",
            "delivery_datetime_ist",
            "days_taken",
            "shipment_weight_kg",
            "pickup_pincode",
            "pickup_city",
            "pickup_state",
            "drop_pincode",
            "drop_city",
            "drop_state",
            "delivery_attempts"
        ]]
        log_and_print(f"transform(data) complete. Shape: {df.shape}", "info")
        return df
    except Exception as e:
        log_and_print(f"transform(data) failed: {e}", "error")
        raise
