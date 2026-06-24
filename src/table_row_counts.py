import sqlite3
import pandas as pd

conn = sqlite3.connect("database/bluestock_mf.db")

tables = ["dim_fund", "dim_date", "fact_nav", "fact_transactions", "fact_performance"]
for table in tables:
    result = pd.read_sql(
    f"select count(*) from {table}", conn)
    print(table)
    print(result)
