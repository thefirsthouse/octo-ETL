import pandas as pd


def load(data: pd.DataFrame, output_path: str):
    """Load converted CSV to user's path"""

    data.to_csv(output_path, index=False)