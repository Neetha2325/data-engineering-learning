-- CTE
-- Return all orders over $200
Select ord.order_id,
sum(ord.units * prd.unit_price) as total_amount_spent
from orders ord left join products prd
on	ord.product_id=prd.product_id 
group by ord.order_id 
having total_amount_spent>200
order by total_amount_spent desc;

-- Return the number of orders over $200
With total_orders_over_200 as 
(Select ord.order_id,
sum(ord.units * prd.unit_price) as total_amount_spent
from orders ord left join products prd
on	ord.product_id=prd.product_id 
group by ord.order_id 
having total_amount_spent>200
order by total_amount_spent desc)
select count(*) from total_orders_over_200;

-- Multiple CTEs
-- List all factories along with no.of products from each factory
With fp as (Select factory,product_name from products),
	 fn as (Select factory,count(product_id) as num_prod from products group by factory)
Select fp.factory,fp.product_name,fn.num_prod 
from fp left join fn 
on fp.factory=fn.factory
order by fp.factory,fp.product_name;

-- Recursive CTE 
-- Return all the dates along with the stock price for that day
-- Return dates even if stock prices are missing
With RECURSIVE recur_cte as 
(
Select '2025-11-01' as dt
union all 
Select dt+Interval 1 DAY 
from recur_cte
where dt<'2025-11-06'
)
select * from 
recur_cte rc left join stock_prices sp 
on rc.dt=sp.date;

Select * from recur_cte;


-- Recursive CTE 
-- Return the reporting chain of each employee 

WITH RECURSIVE emp_hierarchy as (
Select employee_id,employee_name,manager_id,employee_name as hierarchy 
from employees where manager_id is null
UNION ALL
select emp.employee_id,emp.employee_name,emp.manager_id,
concat(emp_hier.hierarchy,'>',emp.employee_name) as hierarchy 
from employees emp inner join emp_hierarchy emp_hier 
on emp_hier.employee_id=emp.manager_id
)
Select * from emp_hierarchy;


