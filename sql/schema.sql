create table dim_fund (scheme_code int primary key, 
scheme_name text,
amc text,
category text);

create table dim_date (date_id int primary key,
full_date date,
year int,
month int,
quarter int);

create table fact_nav (nav_id int primary key autoincrement,
scheme_code int,
date date,
nav float,
foreign key(scheme_code)
references dim_fund(scheme_code));

create table fact_transactions (transaction_id text primary key,
investor_id text,
scheme_code int,
transaction_date date,
transaction_type text,
amount float,
state text,
kyc_status text,
foreign key (scheme_code)
references dim_fund(scheme_code));

create table fact_performance (performance_id int primary key autoincrement,
scheme_code int,
return_1y float,
return_3y float,
return_5y float,
sharpe float,
sortino float,
beta float,
alpha float,
max_drawdown float,
var95 float,
foreign key (scheme_code)
references dim_fund(scheme_code));

create table fact_aum (aum_id int primary key autoincrement,
scheme_code int,
aum float,
foreign key (scheme_code)
references dim_fund(scheme_code));