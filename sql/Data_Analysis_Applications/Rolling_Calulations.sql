--  ROLLING CALCULATIONS

-- Include the subtotals
SELECT	 customer_name, order_date, COUNT(price) AS total_sales
FROM	 pizza_orders
GROUP BY customer_name, order_date WITH ROLLUP;

-- Calculate the cumulative sales over time
WITH ts AS (SELECT	 order_date, SUM(price) AS total_sales
			FROM	 pizza_orders
			GROUP BY order_date
			ORDER BY order_date)
SELECT	order_date,
		SUM(total_sales) OVER(ORDER BY order_date) AS cumulative_sum
FROM 	ts;


-- Update the function to a moving average calculation
SELECT	 country, year, happiness_score,
		 ROUND(AVG(happiness_score)
         OVER (PARTITION BY country ORDER BY year
			   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 3) AS row_num
FROM 	 happiness_scores
ORDER BY country, year;


-- 3. Calculate the 3 year moving average of happiness scores for each country
SELECT	 country, year, happiness_score,
		 ROUND(AVG(happiness_score)
         OVER (PARTITION BY country ORDER BY year
			   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 3) AS row_num
FROM 	 happiness_scores
ORDER BY country, year;




-- Add on the cumulative sum and 6 month moving average

With base_cte as (
Select year(o.order_date) as year,month(o.order_date) as month,
sum(o.units*p.unit_price) as total_sales
 from orders o left join products p
on o.product_id=p.product_id
group by year(o.order_date),month(o.order_date)
order by year(o.order_date),month(o.order_date))

select 
year,month,total_sales,
sum(total_sales) over(order by year,month) as cum_sales,
round(avg(total_sales) over(order by year,month 
							rows BETWEEN 5 PRECEDING and CURRENT ROW),2) as six_mnth_avg_sales
from base_cte;
