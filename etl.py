"""
etl.py
CLI orchestration for the shipment ETL pipeline.
"""
import argparse
import sys
from src.extract import extract, ExtractValidationError
from src.transform import transform
from src.load import load
from src.utils import log_and_print


def main():
    parser = argparse.ArgumentParser(description="Shipment ETL Pipeline")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--out-detail", required=True, help="Path to output detail CSV")
    parser.add_argument("--out-summary", required=True, help="Path to output summary CSV")
    args = parser.parse_args()

    log_and_print("ETL pipeline started", "info")
    try:
        data = extract(args.input)
        df = transform(data)
        load(df, args.out_detail, args.out_summary)
        log_and_print("ETL pipeline completed successfully", "info")
    except ExtractValidationError as e:
        log_and_print(f"ETL failed: {e}", "error")
        sys.exit(1)
    except Exception as e:
        log_and_print(f"ETL failed: {e}", "error")
        sys.exit(1)

if __name__ == "__main__":
    main()
