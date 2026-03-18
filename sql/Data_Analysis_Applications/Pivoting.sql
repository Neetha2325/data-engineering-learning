-- PIVOTING


-- Create a summary table of categories & pizza types
SELECT 	 category,
		 SUM(CASE WHEN crust_type = 'Standard Crust' THEN 1 ELSE 0 END) AS standard_crust,
         SUM(CASE WHEN crust_type = 'Thin Crust' THEN 1 ELSE 0 END) AS thin_crust,
         SUM(CASE WHEN crust_type = 'Gluten-Free Crust' THEN 1 ELSE 0 END) AS gluten_free_crust
FROM 	 pizza_table
GROUP BY category;

-- Create the final summary table
Select g.department,
		round(avg(case when s.grade_level=9 then g.final_grade  end)) as freshman,
        round(avg(case when s.grade_level=10 then g.final_grade  end)) as sophomore,
        round(avg(case when s.grade_level=11 then g.final_grade  end)) as junior,
        round(avg(case when s.grade_level=12 then g.final_grade  end)) as senior
from students s inner join student_grades g 
on s.id=g.student_id
group by g.department
order by g.department; 