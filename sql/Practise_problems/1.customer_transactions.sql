#Return customer ids who do not have any transaction in last 30 days assuming today is '2024-03-01'
With base_cte as 
(Select customer_id,transaction_date,
		row_number() over(partition by customer_id order by transaction_date desc) as rn 
        from transactions)
Select customer_id from base_cte where rn=1 and 
transaction_date <'2024-01-31';