Select customer_id, order_id, order_date,transaction_id,
	row_number() over(partition by customer_id order by transaction_id) as row_num 
from orders
order by customer_id,transaction_id;