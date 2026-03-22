
-- Imputing null values
-- replace the NULL values in the price column 4 different ways 

With Recursive 
recur_cte(dt) as (
			Select '2024-11-01' as dt 
			union 
			Select dt+interval 1 day
			from recur_cte
			where dt<'2024-11-06'
			),
	result as	(
			select r.dt,s.price
			from recur_cte r left join stock_prices s
			on r.dt=s.date
			order by r.dt
			) 
select dt,price,
-- 1. With a hard coded value
		coalesce(price,600) as updated_hard_code_val,
-- 2. With a subquery
		coalesce(price,round((select avg(price) from result),2)) as updated_avg_price,
-- 3. With one window function
		coalesce(price,lag(price)over()) as updated_prior_price,
-- 4. With two window functions
		coalesce(price,round((lead(price) over()+lag(price)over())/2),2) as updated_sum
 from result ;