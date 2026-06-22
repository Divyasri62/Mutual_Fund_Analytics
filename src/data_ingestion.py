import pandas as pd
import os
for file in os.listdir("data/raw"):
    df = pd.read_csv(f"data/raw/{file}")

    print(f"File: {file}")
    print("Shape:", df.shape)
    print("Data types:")
    print(df.dtypes)
    print("First 5 rows:")
    print(df.head())