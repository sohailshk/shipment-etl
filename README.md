
# Shipment ETL Pipeline

## Overview
This project implements a robust, production-quality ETL (Extract, Transform, Load) pipeline for shipment-tracking data in JSON format. The pipeline is designed for reliability, maintainability, and extensibility, with full logging, test coverage, and strict adherence to assignment and industry standards.

## Features
- **Robust ETL pipeline**: Modularized into `extract`, `transform`, and `load` stages.
- **Detailed and summary outputs**: Generates a detailed shipment CSV and a summary statistics CSV.
- **Comprehensive logging**: All actions and errors are logged to both the console and `LOG.md`.
- **Edge case handling**: Handles missing fields, multiple event types, and complex datetime and postal code extraction.
- **Test coverage**: Unit tests for all modules and edge cases using `pytest`.

## Architecture

```
data/raw/shipments.json
        │
        ▼
   [extract.py]
        │
        ▼
   [transform.py]
        │
        ▼
   [load.py]
        │
        ▼
data/processed/detail.csv, summary.csv
```

## ETL Process

### 1. Extract (`src/extract.py`)
- Reads and validates the input JSON file.
- Ensures the top-level structure is a list and each record contains `trackDetails`.
- Logs all actions and raises custom exceptions for invalid data.

### 2. Transform (`src/transform.py`)
- Flattens nested shipment data and extracts all required fields.
- **Postal code extraction**: Robustly extracts pickup and drop postal codes from both main addresses and relevant events.
- **Datetime handling**: Extracts pickup, delivery, and Out for Delivery (OD) datetimes, converting all to local IST (Asia/Kolkata) format.
- **Out for Delivery logic**: Only the latest (most recent) OD event datetime is included per shipment, deduplicated and formatted as a single value.
- **Metrics**: Computes days taken for delivery and counts all delivery attempts (OD + DL events).
- Handles missing or malformed data gracefully.

### 3. Load (`src/load.py`)
- Writes the detailed shipment DataFrame to CSV (`detail.csv`).
- Computes and writes summary statistics (mean, median, mode for days taken and delivery attempts) to CSV (`summary.csv`).
- Logs all file operations.

## Output Files

- **Detail CSV** (`data/processed/detail.csv`):
    - Columns: `tracking_number`, `payment_type`, `pickup_datetime_ist`, `delivery_datetime_ist`, `days_taken`, `shipment_weight_kg`, `pickup_pincode`, `pickup_city`, `pickup_state`, `drop_pincode`, `drop_city`, `drop_state`, `out_for_delivery_datetimes`, `delivery_attempts`
    - Each row represents a shipment, with all datetimes in IST and only the latest OD event included.
- **Summary CSV** (`data/processed/summary.csv`):
    - Columns: `days_mean`, `days_median`, `days_mode`, `att_mean`, `att_median`, `att_mode`
    - Provides aggregate statistics for delivery duration and attempts.

## Logging
All operations, including errors and key steps, are logged to `LOG.md` with timestamps and log levels. This ensures full traceability and auditability.

## Testing
- Unit tests for each module (`extract`, `transform`, `load`) are provided in the `tests/` directory.
- Tests cover normal cases, edge cases, and error conditions.
- Run all tests with:

```bash
pytest --maxfail=1 --disable-warnings -q
```

## Setup & Usage

1. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Run the ETL pipeline:**

    ```bash
    python etl.py --input data/raw/shipments.json --out-detail data/processed/detail.csv --out-summary data/processed/summary.csv
    ```

3. **Check logs:**
    - Review `LOG.md` for a full audit trail of ETL operations.

4. **Run tests:**

    ```bash
    pytest --maxfail=1 --disable-warnings -q
    ```

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies (pandas, python-dateutil, pytz, pytest, etc.)

## Project Structure

```
etl.py
src/
    extract.py
    transform.py
    load.py
    utils.py
tests/
    test_extract.py
    test_transform.py
    test_load.py
data/
    raw/shipments.json
    processed/detail.csv
    processed/summary.csv
LOG.md
README.md
requirements.txt
```

## Contact & Attribution
Author: [Mohammad Sohail]
---
This project follows best practices for Python ETL pipelines, including modularity, logging, and test-driven development. For questions or contributions, please open an issue or pull request.
