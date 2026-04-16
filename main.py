import argparse

from pipeline import run_pipeline


def parse_args():
    parser = argparse.ArgumentParser(description="ETL pipeline for orders data")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    run_pipeline(
        input_path=args.input,
        output_path=args.output
    )
