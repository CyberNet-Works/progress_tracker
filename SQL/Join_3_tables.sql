--! SQL
--Join_3_Tables.sql

SELECT 
    c.customer_id, 
    c.first_name,
    c.last_name,
    CASE 
        WHEN SUM(p.amount) >= 300 THEN 'Paid'
        WHEN SUM(p.amount) < 300 THEN 'Unpaid' 
    END AS payment_status
    
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Payments p ON o.order_id = p.order_id
GROUP BY c.customer_id, c.first_name, c.last_name;


/*
Challenge:
Join 3 Tables
Hard
Problem Description
Consider the following three tables:

Table - Customers

customer_id	first_name	last_name
1	Dwayne	Johnson
2	Randy	Orton
3	John	Cena
Table - Orders

order_id	customer_id	order_date
1	1	2023-07-06
2	2	2023-07-06
3	3	2023-07-09
Table - Payments

payment_id	order_id	amount
1	1	200
2	2	300
3	3	400
Task: Retrieve the customer_id, first_name, last_name, and a column called payment_status which should display:

Paid if the total amount of payments for a customer is greater than or equal to 300.
Unpaid if the total amount of payments for a customer is less than 300.
Expected Result

customer_id	first_name	last_name	payment_status
1	Dwayne	Johnson	Unpaid
2	Randy	Orton	Paid
3	John	Cena	Paid
*/