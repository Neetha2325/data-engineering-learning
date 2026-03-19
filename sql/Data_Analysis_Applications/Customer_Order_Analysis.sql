-- Customer Orders Analysis
-- Find for each customer:First order date,Latest order date,Total amount spent
SELECT 
    customer_id,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS latest_order_date,
    SUM(amount) AS total_amount
FROM customer_orders
GROUP BY customer_id;

-- Find the difference in days between first and second order for each customer.
WITH ranked_orders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS rn
    FROM customer_orders
)

SELECT 
    o1.customer_id,
    DATEDIFF(o2.order_date, o1.order_date) AS days_diff
FROM ranked_orders o1
LEFT JOIN ranked_orders o2
    ON o1.customer_id = o2.customer_id
WHERE o1.rn = 1
  AND o2.rn = 2;
  
-- Find customers whose:latest order amount > first order amount

WITH base_cte AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date ASC
        ) AS first_rn,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date DESC
        ) AS last_rn
    FROM customer_orders
)

SELECT f.customer_id
FROM base_cte f 
JOIN base_cte l
    ON f.customer_id = l.customer_id
WHERE f.first_rn = 1 
  AND l.last_rn = 1 
  AND l.amount > f.amount;