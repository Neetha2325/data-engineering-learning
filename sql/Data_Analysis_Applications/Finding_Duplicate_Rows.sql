-- 1.Duplicate Rows
-- Return student ids, names and emails, excluding duplicates students
With cte1 as (
				select id,student_name,email,
				row_number() over(partition by student_name) as row_num
				from students
			)
select id,student_name,email from cte1
where row_num=1;

-- View duplicate employees

-- 1. View duplicate employees
SELECT	 employee_name, COUNT(*) AS dup_count
FROM	 employee_details
GROUP BY employee_name
HAVING	 COUNT(*) > 1;

-- 2. View duplicate region + employee combos
SELECT	 region, employee_name, COUNT(*) AS dup_count
FROM	 employee_details
GROUP BY region, employee_name
HAVING	 COUNT(*) > 1;

-- 3. View fully duplicate rows
SELECT	 region, employee_name, salary, COUNT(*) AS dup_count
FROM	 employee_details
GROUP BY region, employee_name, salary
HAVING	 COUNT(*) > 1;

-- Exclude duplicate rows

-- 1. Exclude fully duplicate rows
SELECT	DISTINCT region, employee_name, salary
FROM	employee_details;

-- 2. Exclude partially duplicate rows (unique employee name for each row)
SELECT * FROM

(SELECT	region, employee_name, salary,
		ROW_NUMBER() OVER(PARTITION BY employee_name ORDER BY salary DESC) AS top_sal
FROM	employee_details) AS ts

WHERE top_sal = 1;

-- 3. Exclude partially duplicate rows (unique region + employee name for each row)
SELECT * FROM

(SELECT	region, employee_name, salary,
		ROW_NUMBER() OVER(PARTITION BY region, employee_name ORDER BY salary DESC) AS top_sal
FROM	employee_details) AS ts

WHERE top_sal = 1;