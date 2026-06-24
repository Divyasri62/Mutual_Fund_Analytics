import sqlite3
import pandas as pd

connection = sqlite3.connect("database/bluestock_mf.db")

with open("sql/queries.sql","r") as file:
    sql_script = file.read()

queries = sql_script.split(";")

for i, query in enumerate(queries):
    if query.strip():
        print("QUERY", i+1)
        print("================")
        result = pd.read_sql_query(
            query,
            connection
        )
        print(result)

connection.close()