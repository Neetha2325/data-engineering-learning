-- Row_Number()

-- For each customer, add a column for transaction number
select  customer_id, transaction_id,order_id, order_date,
row_number() over(partition by customer_id order by transaction_id) as transaction_number
 from orders;
 

-- Dense_Rank()

-- For each order, rank the products from most units to fewest units
-- If there's a tie, keep the tie and don't skip to the next number after
Select order_id,product_id,units,
		dense_rank() over(partition by order_id order by units desc) as prd_rank
        from orders;

-- lag
-- For each customer, find the change in units per order over time
With my_cte as (
select 
customer_id,order_id,
sum(units)as total_units,
min(transaction_id) as min_td  
from orders
group by customer_id,order_id
order by customer_id,order_id,min_td
),
prior_cte as (Select customer_id,order_id,total_units,
				lag(total_units) 
                over(partition by customer_id order by min_td) as prior_units
				from my_cte
                ),
next_cte as (Select customer_id,order_id,total_units,
				lead(total_units) 
                over(partition by customer_id order by min_td) as next_units
				from my_cte
                )
Select pc.customer_id,pc.order_id,pc.total_units,pc.prior_units,nc.next_units,
		pc.total_units-pc.prior_units diff_in_prior_and_total_units
        from prior_cte pc inner join next_cte nc
        on pc.customer_id=nc.customer_id and pc.order_id=nc.order_id;
        
-- ntile
-- Return the top 1% of customers in terms of spending
With my_cte as 
				(
				Select o.customer_id,sum(o.units*p.unit_price) as total_amt
				from orders o
				left join products p 
				on o.product_id=p.product_id
				group by customer_id
				order by total_amt desc),
percent_cte as (
				Select customer_id,total_amt,
                ntile(100) over (order by total_amt desc) as percent
				from my_cte)
select customer_id,total_amt,percent from percent_cte
where percent=1;


