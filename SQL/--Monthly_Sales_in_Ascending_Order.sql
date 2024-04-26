--Monthly_Sales_in_Ascending_Order.SQL

SELECT
    SUBSTR(sales_date,6, 2) AS month,
    sum(sales_amount) AS total_sales

FROM Sales
GROUP BY month;

/*
Monthly Sales in Ascending Order
Medium
Problem Description
Consider the following:

Table - Sales

sales_id	sales_date	sales_amount
1	2023-05-30	50000
2	2023-06-03	80000
3	2023-06-23	100000
4	2023-06-30	90000
5	2023-06-22	800
Task: Find the monthly sales from the above table and sort them in ascending order of sales_amount and sales_date. Use the aliases month and total_sales for the result.

month	total_sales
05	50000
06		270800
*/