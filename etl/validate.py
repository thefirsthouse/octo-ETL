import pandas as pd

from config import REQUIRED_COLUMNS


def validate(data: pd.DataFrame) -> pd.DataFrame:
    """Validate the data and return only valid rows"""

    if data.empty:
        raise ValueError("Input data is empty. Cannot validate.")
    
    required_columns = REQUIRED_COLUMNS
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    return data
