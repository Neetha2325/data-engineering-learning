
-- MIN / MAX VALUE FILTERING

-- Number of sales on most recent date: Group by + join approach
WITH rd AS (SELECT	 sales_rep, MAX(date) AS most_recent_date
			FROM	 sales
			GROUP BY sales_rep)
            
SELECT	rd.sales_rep, rd.most_recent_date, s.sales
FROM	rd LEFT JOIN sales s
		ON rd.sales_rep = s.sales_rep
        AND rd.most_recent_date = s.date;
                
-- Number of sales on most recent date: Window function approach
SELECT * FROM

(SELECT	sales_rep, date, sales,
		ROW_NUMBER() OVER (PARTITION BY sales_rep ORDER BY date DESC) AS row_num
FROM	sales) AS rn

WHERE row_num = 1;

-- Return each student's top grade and corresponding class
With base_cte as (
		Select student_id,final_grade,class_name,
		dense_rank() over(partition by student_id order by final_grade desc) as grade_ordered
		from student_grades
        )
select stud.id,stud.student_name,final_grade,class_name
from students stud left join base_cte stud_gd
on stud.id=stud_gd.student_id
where stud_gd.grade_ordered=1;