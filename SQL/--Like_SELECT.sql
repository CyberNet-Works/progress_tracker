--Like_SELECT.sql
SELECT name
FROM Employees
WHERE name LIKE '_%e%_'

ORDER BY salary ASC
;
/*
Challenge:
Ascending Order of Salaries
Easy
Problem Description
Consider the following table:

Table - Employees

emp_id	name	department	salary
1	Bryant	Sales	90000
2	Steph	Content	30000
3	Hakeem	Development	40000
4	Shaquille	Sales	20000
5	Michael 	Sales	90000
Task: Retrieve the names of all employees who've got e in the middle of their names in ascending order of their salaries.

name
Steph
Hakeem
Michael

*/
