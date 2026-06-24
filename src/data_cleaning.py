import pandas as pd
import numpy as np

nav = pd.read_csv("c:/Users/Divya/Downloads/MutualFundAnalytics_Project_1/data/raw/nav_history.csv")

print(nav.head())
print(nav.info())

nav["Date"] = pd.to_datetime(nav["Date"])  #converting dtype
print(nav.dtypes)

nav["NAV"] = nav["NAV"].ffill()  #Filling missing values
print("Null values:", nav["NAV"].isnull().sum())

nav = nav.drop_duplicates() #removing duplicates
print("Duplicates:", nav.duplicated().sum())

nav.to_csv("c:/Users/Divya/Downloads/MutualFundAnalytics_Project_1/data/processed/clean_nav_history.csv",index=False)


tran = pd.read_csv("c:/Users/Divya/Downloads/MutualFundAnalytics_Project_1/data/raw/investor_transactions.csv")

print(tran.head())
print(tran.info())

tran["transaction_type"] = (tran["transaction_type"].str.upper())    #standardized values

print(tran[tran["amount"] <= 0])   #validating amount

tran["transaction_date"] = pd.to_datetime(tran["transaction_date"])   #converting dtype
print(tran.dtypes)

print(tran["kyc_status"].unique())  

tran = tran.drop_duplicates() #removing duplicates

tran.to_csv("data/processed/clean_investor_transactions.csv",index=False)



perf = pd.read_csv("data/raw/scheme_performance.csv")

print(perf.head())
print(perf.info())

print(perf.columns)

return_columns = ["return_1y","return_3y","return_5y"]   #validate all return values are numeric
for col in return_columns:
    perf[col] = pd.to_numeric(perf[col])

print(perf[(perf["return_1y"] > 100) |(perf["return_1y"] < -100)])   #flag anomalies

perf = perf.drop_duplicates() #removing duplicates

perf.to_csv("data/processed/clean_scheme_performance.csv",index=False)



fund = pd.read_csv("data/raw/fund_master.csv")

print(fund.head())
print(fund.columns)

fund = fund.rename(columns={"Scheme_Code": "scheme_code", "Scheme_Name": "scheme_name", "AMC": "amc", "Scheme_Category": "category", "Average_AUM_Cr": "aum"})

dim_fund = fund[["scheme_code", "scheme_name", "amc", "category"]]

dim_fund = dim_fund.drop_duplicates()

dim_fund = dim_fund.dropna(subset=["scheme_code"])  #removing missing schemecodes


dim_fund.to_csv("data/processed/clean_fund_master.csv", index=False)



aum = fund[["scheme_code", "aum"]]

aum["aum"] = pd.to_numeric(aum["aum"], errors="coerce")

aum = aum.dropna(subset=["aum"])  #removing missing AUM

aum = aum[aum["aum"] > 0]

aum = aum.drop_duplicates()

aum.to_csv("data/processed/clean_aum.csv", index=False)