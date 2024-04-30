SELECT SUBSTR(sales_date, 6, 2) AS month,
SUM(sales_amount) AS total_sales
FROM Sales

GROUP BY month

ORDER BY total_sales DESC, month;

/*
Challenge:
Order Delivery in Exactly 3 Days
Medium
Problem Description
Consider the following table:

Table - Orders

order_id	customer_id	order_date	delivery_date
1	1001	2023-04-15	2023-04-18
2	1002	2023-05-10	2023-05-15
3	1003	2023-05-01	2023-05-06
4	1004	2023-04-25	2023-04-30
5	1005	2023-05-15	2023-05-18
Task: Retrieve the number of orders that were delivered in exactly 3 days of the order date. Use the alias num_orders to return the count of the orders.

num_orders
2
*/