
--Top_3_Highest_Paid_Employees


SELECT name
FROM Employees
WHERE 
    type = "Full-Time" AND 
    department = "Sales" AND
    experience >= 5 AND
    salary > 5000
ORDER BY salary DESC;

/*
Problem Description
Consider the following table:

Table - Employees

emp_id	name	department	salary	type	experience
1	Dave	Sales	3000	Full-Time	2
2	Rey	Sales	6000	Full-Time	6
3	Dwayne	Sales	6000	Freelance	8
4	John	Development	6000	Part-Time	7
5	Paul	Sales	7000	Full-Time	6
Task: Retrieve the names of the top 3 highest-paid full-time employees in the Sales department with a salary greater than $5,000 and experience is greater than or equal to 5 years. Order the result by their salary in descending order.

Expected Result

name
Paul
Rey
*/