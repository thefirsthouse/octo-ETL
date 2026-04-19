import sqlite3

import pandas as pd


def aggregate(data: pd.DataFrame):
    """Aggegate data using SQLite"""

    conn = sqlite3.connect(':memory:')
    data.to_sql('orders', conn, index=False, if_exists='replace')
    query = """
    SELECT
        user_id,
        SUM(total) AS total_spent
    FROM orders
    GROUP BY user_id"""

    result = pd.read_sql(query, conn)
    conn.close()

    return result