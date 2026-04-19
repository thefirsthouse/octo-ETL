import pandas as pd


def extract(file_path: str) -> pd.DataFrame:
    """Extract data from a CSV file and return it as a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pd.DataFrame()
