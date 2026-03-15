-- left Join
Select ps.product_id,ps.product_name,os.product_id as product_in_orders
		from products ps left join orders os  
		on os.product_id=ps.product_id
        where os.product_id is null;
        
-- Self Joins
select p1.product_name,p1.unit_price,
		p2.product_name,p2.unit_price,
        (p1.unit_price-p2.unit_price) AS price_diff
 from products p1 inner join products p2 
on p1.product_id<>p2.product_id
where  ABS(p1.unit_price-p2.unit_price)<0.25;

-- CROSS JOIN
select p1.product_name,p1.unit_price,
		p2.product_name,p2.unit_price,
        (p1.unit_price-p2.unit_price) AS price_diff
 from products p1 cross join products p2 
where p1.product_id<>p2.product_id
and  ABS(p1.unit_price-p2.unit_price)<0.25;


-- Union and Union all 
Select * from tops 
union 
select * from outerwear;

Select * from tops 
union all
select * from outerwear;