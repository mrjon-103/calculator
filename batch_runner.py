"""Supplied CSV runner. You may use this file unchanged and acknowledge it.

Example: python3 batch_runner.py data/normal.csv results.csv
Complete process_calculation in batch_calculator.py before running a batch.
"""

import argparse
import csv
from pathlib import Path
import sys

from batch_calculator import process_calculation


def run_batch(input_path, output_path):
    """Handle files and the loop; delegate calculation logic to the student."""
    if Path(input_path).resolve() == Path(output_path).resolve():
        raise ValueError("Use different input and output files")

    with open(input_path, encoding="utf-8", newline="") as input_file:
        reader = csv.reader(input_file)
        if next(reader, None) != ["operation", "a", "b"]:
            raise ValueError("The input header must be operation,a,b")
        records = list(reader)

    results = []
    for number, record in enumerate(records, start=1):
        if len(record) != 3:
            raise ValueError("Each data record must have exactly three fields")
        status, result, error_code = process_calculation(record[0], record[1], record[2])
        results.append((number, status, result, error_code))
        if status == "ERROR":
            print(f"Record {number}: {error_code}", file=sys.stderr)

    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["row", "status", "result", "error_code"])
        writer.writerows(results)

    succeeded = sum(record[1] == "OK" for record in results)
    failed = sum(record[1] == "ERROR" for record in results)
    print(f"Processed {len(results)} records: {succeeded} succeeded, {failed} failed.")


def main():
    parser = argparse.ArgumentParser(description="Process a CSV of calculator inputs")
    parser.add_argument("input", help="CSV with the operation,a,b header")
    parser.add_argument("output", help="Where to write result records")
    args = parser.parse_args()
    try:
        run_batch(args.input, args.output)
    except (OSError, ValueError) as error:
        print(f"Batch error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
