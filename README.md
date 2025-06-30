# Shipment ETL Pipeline

## Overview
This project provides a clean, maintainable, end-to-end ETL pipeline for a shipment-tracking JSON dataset. It reads, validates, transforms, and loads shipment data, producing detailed and summary CSVs. All actions are logged in `LOG.md`.

## Setup

1. **Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run the ETL pipeline:**

```bash
python etl.py --input data/raw/shipments.json --out-detail data/processed/detail.csv --out-summary data/processed/summary.csv
```

3. **Run tests:**

```bash
pytest --maxfail=1 --disable-warnings -q
```

## Logging
All operations are logged to `LOG.md` with timestamps and details.
