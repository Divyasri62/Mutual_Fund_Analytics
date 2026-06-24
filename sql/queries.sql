-- top 5 funds by AUM
select f.scheme_name, f.amc, a.aum
from fact_aum a
join dim_fund f
on a.scheme_code = f.scheme_code
order by a.aum desc
limit 5;

-- average NAV per month
select strftime('%Y-%m', date) as month, avg(nav) as avg_nav
from fact_nav
group by month
order by month;

-- SIP YoY growth
select strftime('%Y', transaction_date) as year, count(*) as sip_count, sum(amount) as total_amount
from fact_transactions
where transaction_type = 'SIP'
group by year
order by year;

-- transactions by state
select state, count(transaction_id) as total_transactions, SUM(amount) as total_amount
from fact_transactions
group by state
order by total_transactions desc;

-- highest rank funds ON beta
select f.scheme_name, p.beta
from fact_performance p
join dim_fund f
ON p.scheme_code = f.scheme_code
order by p.beta desc;

-- fund count based on AMC
select amc, count(scheme_code) as total_funds
from dim_fund
group by amc
order by total_funds desc;

-- each transcations count
select transaction_type, count(*) as total_transactions, sum(amount) as total_amount
from fact_transactions
group by transaction_type;