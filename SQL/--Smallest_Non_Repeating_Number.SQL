--Smallest_Non_Repeating_Number.SQL

SELECT MIN(number) AS smallest_single_number
FROM (
    SELECT number
    FROM Numbers
    GROUP BY number
    HAVING COUNT(number) = 1
);

/*
Smallest Non-Repeating Number
Medium
Problem Description
Consider the following table:

Table - Numbers

number
8
8
3
3
1
4
5
6
Task: Write an SQL query to fetch the smallest non-repeating number. If there is no such number, fetch NULL. Use the alias smallest_single_number.

Expected Result

smallest_single_number
1
*/
