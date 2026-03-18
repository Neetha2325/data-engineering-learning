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
