import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()
nav_data = data["data"]
df = pd.DataFrame(nav_data)

df.to_csv("data/raw/HDFC_nav.csv",index=False)

print(df.head())
print(df.shape)