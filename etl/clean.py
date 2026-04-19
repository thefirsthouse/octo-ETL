import pandas as pd


def clean(data: pd.DataFrame):
    """Clean the data by removing invalid and inconsistent rows."""

    data = data.dropna(subset=["user_id", "price", "quantity", "date"])

    data = data.drop_duplicates()

    data = data[(data["price"] > 0) & (data["quantity"] > 0)]

    data = data.copy()
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data = data.dropna(subset=["date"])

    return data