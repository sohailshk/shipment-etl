# ETL Pipeline Log

All actions, function calls, and errors will be logged here with timestamps.
[2025-06-30 18:33:16] ETL pipeline started
[2025-06-30 18:33:16] Starting extract(path=data/raw/shipments.json)
[2025-06-30 18:33:16] extract(path=data/raw/shipments.json) succeeded with 99 records.
[2025-06-30 18:33:16] Starting transform(data)
[2025-06-30 18:33:19] transform(data) complete. Shape: (99, 13)
[2025-06-30 18:33:19] Starting load(detail_out=data/processed/detail.csv, summary_out=data/processed/summary.csv)
[2025-06-30 18:33:19] Detail CSV written to data/processed/detail.csv
[2025-06-30 18:33:19] Summary CSV written to data/processed/summary.csv
[2025-06-30 18:33:19] ETL pipeline completed successfully
[2025-06-30 18:33:31] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_extract_valid0\input.json)
[2025-06-30 18:33:31] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_extract_valid0\input.json) succeeded with 1 records.
[2025-06-30 18:33:31] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_extract_missing_trackdeta0\input.json)
[2025-06-30 18:33:31] Missing 'trackDetails' in record 0
[2025-06-30 18:33:31] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_extract_missing_trackdeta0\input.json) failed: Missing 'trackDetails' in record 0
[2025-06-30 18:33:31] Starting load(detail_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_load_creates_csvs0\detail.csv, summary_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_load_creates_csvs0\summary.csv)
[2025-06-30 18:33:31] Detail CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_load_creates_csvs0\detail.csv
[2025-06-30 18:33:31] Summary CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-0\test_load_creates_csvs0\summary.csv
[2025-06-30 18:33:31] Starting transform(data)
[2025-06-30 18:33:31] transform(data) complete. Shape: (1, 13)
[2025-06-30 18:33:31] Starting transform(data)
[2025-06-30 18:33:31] transform(data) complete. Shape: (1, 13)
[2025-06-30 18:33:31] Starting transform(data)
[2025-06-30 18:33:31] transform(data) complete. Shape: (1, 13)
[2025-06-30 19:12:58] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_extract_valid0\input.json)
[2025-06-30 19:12:58] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_extract_valid0\input.json) succeeded with 1 records.
[2025-06-30 19:12:58] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_extract_missing_trackdeta0\input.json)
[2025-06-30 19:12:58] Missing 'trackDetails' in record 0
[2025-06-30 19:12:58] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_extract_missing_trackdeta0\input.json) failed: Missing 'trackDetails' in record 0
[2025-06-30 19:12:58] Starting load(detail_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_load_creates_csvs0\detail.csv, summary_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_load_creates_csvs0\summary.csv)
[2025-06-30 19:12:58] Detail CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_load_creates_csvs0\detail.csv
[2025-06-30 19:12:58] Summary CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-1\test_load_creates_csvs0\summary.csv
[2025-06-30 19:12:58] Starting transform(data)
[2025-06-30 19:13:01] transform(data) complete. Shape: (1, 13)
[2025-06-30 19:13:01] Starting transform(data)
[2025-06-30 19:13:01] transform(data) complete. Shape: (1, 13)
[2025-06-30 19:13:01] Starting transform(data)
[2025-06-30 19:13:01] transform(data) complete. Shape: (1, 13)
[2025-06-30 19:30:00] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_extract_valid0\input.json)
[2025-06-30 19:30:00] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_extract_valid0\input.json) succeeded with 1 records.
[2025-06-30 19:30:00] Starting extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_extract_missing_trackdeta0\input.json)
[2025-06-30 19:30:00] Missing 'trackDetails' in record 0
[2025-06-30 19:30:00] extract(path=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_extract_missing_trackdeta0\input.json) failed: Missing 'trackDetails' in record 0
[2025-06-30 19:30:00] Starting load(detail_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_load_creates_csvs0\detail.csv, summary_out=C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_load_creates_csvs0\summary.csv)
[2025-06-30 19:30:00] Detail CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_load_creates_csvs0\detail.csv
[2025-06-30 19:30:00] Summary CSV written to C:\Users\sohai\AppData\Local\Temp\pytest-of-sohai\pytest-2\test_load_creates_csvs0\summary.csv
[2025-06-30 19:30:00] Starting transform(data)
[2025-06-30 19:30:00] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:30:00] Starting transform(data)
[2025-06-30 19:30:00] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:30:00] Starting transform(data)
[2025-06-30 19:30:00] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:30:38] ETL pipeline started
[2025-06-30 19:30:38] Starting extract(path=data/raw/shipments.json)
[2025-06-30 19:30:38] extract(path=data/raw/shipments.json) succeeded with 99 records.
[2025-06-30 19:30:38] Starting transform(data)
[2025-06-30 19:30:38] transform(data) complete. Shape: (99, 14)
[2025-06-30 19:30:38] Starting load(detail_out=data/processed/detail.csv, summary_out=data/processed/summary.csv)
[2025-06-30 19:30:38] Detail CSV written to data/processed/detail.csv
[2025-06-30 19:30:38] Summary CSV written to data/processed/summary.csv
[2025-06-30 19:30:38] ETL pipeline completed successfully
[2025-06-30 19:41:27] Starting transform(data)
[2025-06-30 19:41:27] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:41:27] Starting transform(data)
[2025-06-30 19:41:27] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:41:27] Starting transform(data)
[2025-06-30 19:41:27] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:41:27] Starting transform(data)
[2025-06-30 19:41:27] transform(data) complete. Shape: (1, 14)
[2025-06-30 19:46:28] ETL pipeline started
[2025-06-30 19:46:28] Starting extract(path=data/raw/shipments.json)
[2025-06-30 19:46:28] extract(path=data/raw/shipments.json) succeeded with 99 records.
[2025-06-30 19:46:28] Starting transform(data)
[2025-06-30 19:46:28] transform(data) complete. Shape: (99, 14)
[2025-06-30 19:46:28] Starting load(detail_out=data/processed/detail.csv, summary_out=data/processed/summary.csv)
[2025-06-30 19:46:28] Detail CSV written to data/processed/detail.csv
[2025-06-30 19:46:28] Summary CSV written to data/processed/summary.csv
[2025-06-30 19:46:28] ETL pipeline completed successfully
