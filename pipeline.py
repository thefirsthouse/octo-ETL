import pandas

import steps


def run_pipeline(input_path: str, output_path: str):
    print("Running pipeline...")
    print("Extracting data...")
    data = steps.extract(input_path)
    print("Validating data...")
    data = steps.validate(data)
    print("Cleaning data...")
    data = steps.clean(data)
    print("Transforming data...")
    data = steps.transform(data)
    print("Aggregating data...")
    data = steps.aggregate(data)
    print("Loading data...")
    steps.load(data, output_path)
    print("Pipeline completed.")
