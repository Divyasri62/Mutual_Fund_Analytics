# Mutual Fund Analytics - Data Dictionary

Database Name: bluestock_mf.db
Database Type: SQLite
Data Source: Cleaned CSV files from data/processed folder.

---

# Table 1: dim_fund

Source:clean_fund_master.csv

| Column | Data Type |
|---|---|
| scheme_code | int |
| scheme_name | text |
| amc | text | 
| category | text |
Business Definition: Stores master information about all mutual fund schemes.

---

# Table 2: dim_date

Source:clean_nav_history.csv

| Column | Data Type |
|---|---|
| date_id | int |
| full_date | date |
| year | int |
| month | int |
| quarter | int |

Business Definition: date dimension used for time-based analysis.

---

# Table 3: fact_nav

Source: clean_nav_history.csv

| Column | Data Type |
|---|---|
| nav_id | int |
| scheme_code | int |
| date | date |
| nav | float |

Business Definition: Stores historical daily NAV values for each mutual fund scheme.

---

# Table 4: fact_transactions

Source: clean_investor_transactions.csv

| Column | Data Type |
|---|---|
| transaction_id | text | 
| investor_id | text | 
| scheme_code | int |
| transaction_date | date |
| transaction_type | text |
| amount | float |
| state | text |
| kyc_status | text |

Business Definition: Stores investor investment activity and transaction details.

---

# Table 5: fact_performance

Source: clean_scheme_performance.csv


| Column | Data Type | 
|---|---|
| performance_id | int |
| scheme_code | int |
| return_1y | float | 
| return_3y | float | 
| return_5y | float | 
| sharpe | float | 
| sortino | float | 
| beta | float | 
| alpha | float |
| max_drawdown |
| var95 | float | 

Business Definition: Stores performance and risk metrics of mutual funds.

---

# Table 6: fact_aum

Source: clean_aum.csv

| Column | Data Type |
|---|---|
| aum_id | int | 
| scheme_code | int |
| aum | float | 

Business Definition: Stores total assets managed by each mutual fund scheme.

