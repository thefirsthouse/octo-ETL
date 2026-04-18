import pandas
from pandas import DataFrame


def extract(file_path: str) -> pandas.DataFrame:
    """Extract data from a CSV file and return it as a DataFrame."""
    try:
        data = pandas.read_csv(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pandas.DataFrame()


def validate(data: DataFrame) -> DataFrame:
    """Validate the data and return only valid rows"""

    if data.empty:
        raise ValueError("Input data is empty. Cannot validate.")
    
    required_columns = {'user_id', 'product', 'price'}
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    return data
