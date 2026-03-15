-- Subqueries in Select 
-- Find avg unit price and diff between unit price and avg unit price for each product
Select product_id, product_name, unit_price,
		(select avg(unit_price)  from products) as avg_price,
		(unit_price-(select avg(unit_price) from products)) as diff 
        from products
        order by product_id;
        
-- Subqueries in from clause 
-- List all the factories and no of products from each factory
Select fp.factory,fp.product_name,fn.num_prod from 
(Select factory,product_name from products) fp 
left join
(Select factory,count(product_id) as num_prod
from products
group by factory) fn
on fp.factory=fn.factory
order by fp.factory,fp.product_name;

-- Subqueries in where clause
-- Return products where the unit price is less than
-- the unit price of all products from Wicked Choccy's

Select * from products 
where unit_price < all(select unit_price from products 
						where factory="Wicked Choccy's")
