-- 1.log 
Select country,population,
log(population),
round(log(population),3)
 from country_stats; 

-- 2.Floor  for binning
With my_cte as 
(Select country,population,
floor(population/10000000)*10 as flr_bin
from country_stats)
select flr_bin,count(country)
from my_cte
group by flr_bin
order by flr_bin;


-- Floor

-- Number of customers in each spend bin
With my_cte as (Select  ord.customer_id,
				sum(ord.units*prd.unit_price) as total_spend,
				floor(sum(ord.units*prd.unit_price)/10)*10 as total_spend_bin
				from orders ord
				left join products prd 
				on ord.product_id=prd.product_id
				group by customer_id)
select total_spend_bin,count(customer_id) 
from my_cte
group by total_spend_bin
order by total_spend_bin;

-- 3.max

-- Return the greatest value of each column
Select max(q1),max(q2),max(q3),max(q4) 
from miles_run;

-- 4.greatest
-- Return the greatest of each row
select greatest(coalesce(q1,0),coalesce(q2,0),coalesce(q3,0),coalesce(q4,0))
 from miles_run;
 
 -- 5.cast
 select str_value,cast(str_value as decimal(5,2)) from sample_table;
 
 -- Turn integer into float 
 Select population,population/10 from country_stats;
 
 
 -- 5.DateTime Functions
 
 Select current_date(),current_timestamp();
 
 -- Extract info about datetime values
 Select event_name,
		event_date,
        year(event_date),month(event_date),dayofweek(event_date)
 from my_events;
 
 -- Spell out the full days of the week using CASE statements
 With my_cte as (Select event_name,
						event_date,
						year(event_date),month(event_date),
                        dayofweek(event_date) as week_day
						from my_events)
Select *,case 
			when week_day=1 then 'SUNDAY'
			when week_day=2 then 'MONDAY'
			when week_day=3 then 'TUESDAY'
            when week_day=4 then 'WEDNESDAY'
            when week_day=5 then 'THURSDAY'
            when week_day=6 then 'FRIDAY'
            when week_day=7 then 'SATURDAY'
		 else 'Unknown'
		 end as day_name
 from my_cte; 
 
 -- Calculate an interval between datetime values
 
 Select event_name,event_date,current_date,
		datediff(event_date,current_date) as date_diff
        from my_events;
        
        
-- Add / subtract an interval from a datetime value
Select event_name,event_datetime,
		date_add(event_datetime,interval 1 hour) as Time_add_val,
		date_sub(event_datetime,interval 1 hour) as Time_sub_val
        from my_events;

-- Add a column called ship_date that adds 2 days to each order date
Select order_id,order_date,
		date_add(order_date,interval 2 day) as ship_date from orders
		where year(order_date)=2024 and month(order_date) between 4 and 6;
        
        
-- 6. String Functions
-- Change the case
Select * from my_events;
select upper(event_name),lower(event_type) from my_events;

-- Clean up event type and find the length of the description
Select distinct event_type from my_events;
Select event_name,trim(replace(event_type,'!','')) as clean_event_type,
		event_desc from my_events;

-- Combine the type and description columns
With base_cte as (
		Select event_name,trim(replace(event_type,'!','')) as clean_event_type,
				event_desc from my_events)
Select event_name,
		concat(clean_event_type,'|',event_desc) as combined_column
        from base_cte;
        
-- substr() and instr()
Select event_name,substr(event_name,1,3) from my_events;
Select event_name,instr(event_name,' ') from my_events;

-- Update to handle single word events
Select event_name,
	case
    when instr(event_name,' ')=0 then event_name
    else substr(event_name,1,instr(event_name,' ')-1)  
    end as first_word
	from my_events;
    
-- Return descriptions that contain 'family'
Select event_name,event_desc from my_events
 where event_desc like '%family%';
 
 -- Return descriptions that start with 'A'
Select event_name,event_desc 
from my_events 
where event_desc like 'A%';

 -- Return students with three letter first names
Select event_name
from my_events
where event_name like '___ %';


 -- Note any celebration word in the sentence
Select event_name,event_desc,
		regexp_substr(event_desc,'celebration|festival|holiday') as category
from my_events
where 
event_desc like '%celebration%' or 
event_desc like '%festival%' or 
event_desc like '%holiday%'; 
  
 
 
 -- Return words with hyphens in them
Select event_desc,
	regexp_substr(event_desc,'([A-Z][a-z]+(-[A-Za-z]+))+') as with_hypens
 from my_events;
