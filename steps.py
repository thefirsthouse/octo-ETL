import pandas as pd


def extract(file_path: str) -> pd.DataFrame:
    """Extract data from a CSV file and return it as a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pd.DataFrame()


def validate(data: pd.DataFrame) -> pd.DataFrame:
    """Validate the data and return only valid rows"""

    if data.empty:
        raise ValueError("Input data is empty. Cannot validate.")
    
    required_columns = {'user_id', 'product', 'price'}
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    return data


def clean(data: pd.DataFrame):
    """Clean the data by removing invalid and inconsistent rows."""

    data = data.dropna(subset=["user_id", "price", "quantity", "date"])

    data = data.drop_duplicates()

    data = data[(data["price"] > 0) & (data["quantity"] > 0)]

    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data = data.dropna(subset=["date"])

    return data


def transform(data: pd.DataFrame):
    """Add new total column"""

    data['total'] = data['price'] * data['quantity']
    return data


def aggregate(data: pd.DataFrame):
    """Generates statistics for each user"""

    result = (
        data.groupby("user_id")["total"]
        .sum()
        .reset_index()
    )

    result = result.rename(columns={"total": "total_spent"})
    return result


def load(data: pd.DataFrame, output_path: str):
    """Load converted CSV to user's path"""

    data.to_csv(output_path, index=False)
