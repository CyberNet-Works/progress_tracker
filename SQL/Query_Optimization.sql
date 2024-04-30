--! SQL
--query_optimization
SELECT 
    SUBSTR(sales_date, 1, 7) AS month,
    sales_id,
    sales_amount AS total_sales_amount
FROM SALES

GROUP BY sales_id

ORDER BY total_sales_amount DESC, month DESC, sales_amount 
LIMIT 4;

/*Query Optimization
Hard
Problem Description
Consider the following table:

Table - Sales

sales_id	sales_date	sales_amount
1	2023-05-30	50000
2	2023-06-03	80000
3	2023-06-23	100000
4	2023-06-30	90000
5	2023-06-22	800
Task: Find the top 3 products (sales_id) with the highest total sales amount for each month, in descending order of the months and the sales amount.

*/