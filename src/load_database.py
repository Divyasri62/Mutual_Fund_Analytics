import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database/bluestock_mf.db")

fund = pd.read_csv("data/processed/clean_fund_master.csv")
fund.to_sql("dim_fund",
engine,
if_exists="append",
index=False)
print("dim_fund loaded")


nav_temp = pd.read_csv("data/processed/clean_nav_history.csv")
nav_temp["Date"] = pd.to_datetime(nav_temp["Date"])
dates = pd.DataFrame()
dates["full_date"] = nav_temp["Date"].unique()
dates["date_id"] = (dates["full_date"].dt.strftime("%Y%m%d").astype(int))
dates["year"] = (dates["full_date"].dt.year)
dates["month"] = (dates["full_date"].dt.month)
dates["quarter"] = (dates["full_date"].dt.quarter)
dates.to_sql("dim_date",
engine,
if_exists="append",
index=False)
print("dim_date loaded")


nav = pd.read_csv("data/processed/clean_nav_history.csv")
nav.to_sql("fact_nav",
engine,
if_exists="append",
index=False)
print("fact_nav loaded")


tran = pd.read_csv("data/processed/clean_investor_transactions.csv")
tran.to_sql("fact_transactions",
engine,
if_exists="append",
index=False)
print("fact_transactions loaded")


perf = pd.read_csv("data/processed/clean_scheme_performance.csv")
perf.to_sql("fact_performance",
engine,
if_exists="append",
index=False)
print('fact_performance loaded')


aum = pd.read_csv("data/processed/clean_aum.csv")
aum.to_sql("fact_aum",
engine,
if_exists="append",
index=False)
print("fact_aum loaded")