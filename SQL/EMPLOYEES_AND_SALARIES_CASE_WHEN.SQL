--EMPLOYEES_AND_SALARIES_CASE_WHEN
SELECT
    e.emp_id,
    first_name,
    last_name,
    CASE
        WHEN s.salary >= 5000 THEN 'High'
        WHEN s.salary >= 4000 THEN 'Medium'
        WHEN s.salary < 4000 THEN 'Low'
    END AS salary_category

FROM Employees e 
JOIN Salaries s ON e.emp_id = s.emp_id


/*
Challenge:
Employees and Salaries
Hard
Problem Description
Consider the following two tables:

Table - Employees

emp_id	first_name	last_name
1	Jaden	Smith
2	Marshall	Mathers
3	Jermaine	Cole
Table - Salaries

emp_id	salary
1	4875
2	6000
3	3800
Task: Retrieve the employee ID, first name, last name, and a column called salary_category which should display:

High for salaries greater than or equal to 5000.
Medium for salaries between 4000 and 4999.
Low for salaries below 4000.
Expected Result

emp_id	first_name	last_name	salary_category
1	Jaden	Smith	Medium
2	Marshall	Mathers	High
3	Jermaine	Cole	Low
*/