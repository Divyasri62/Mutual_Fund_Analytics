# import requests
# import pandas as pd

# url = "https://api.mfapi.in/mf/125497"
# response = requests.get(url)
# data = response.json()
# nav_data = data["data"]
# df = pd.DataFrame(nav_data)

# df.to_csv("data/raw/HDFC_nav.csv",index=False)

# print(df.head())
# print(df.shape)


import requests
import pandas as pd

schemes = {
    "HDFC_Top_100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}


for fund_name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    nav_data = data["data"]
    df = pd.DataFrame(nav_data)
    df.to_csv(
        f"data/raw/{fund_name}_nav.csv",
        index=False
    )

    print(f"{fund_name} completed")