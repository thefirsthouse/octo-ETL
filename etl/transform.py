import pandas as pd


def transform(data: pd.DataFrame):
    """Add new total column"""

    data['total'] = data['price'] * data['quantity']
    return data
