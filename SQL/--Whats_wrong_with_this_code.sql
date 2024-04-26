--Whats_wrong_with_this_code.sql?


CREATE TABLE Students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(20) UNIQUE);
--two unique constraints may be problematic in the future.  Ensure this is what you want.

CREATE TABLE Employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  name VARCHAR(50));
--two name fields, instead use first_name, last_name.  Also consider increasing varchar limit, though I believe its depricated anyhow now.

SELECT *
FROM EPL
WHERE goals >= '50';
--the above uses string comparison instead of numeric.

SELECT *
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;
--vague join, better to be explicit inner join, left join, right join, outer join etc.

SELECT department, COUNT(*)
FROM Employees
GROUP BY department, salary;
--group by is distinct, and the select has both group by and count in same statment, check it is functioning correctly.

SELECT *
FROM Employees
WHERE salary BETWEEN 30000 AND 90000;
--consider being explicit with => =>


 CREATE TABLE Orders (
  id INT PRIMARY KEY,
  customer_id INT,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);
-- WARNING: ON DELETE CASCADE will automatically delete any referencing rows in the Orders table if their corresponding customer is deleted.
-- Use with caution to prevent unintended data loss.


SELECT *
FROM Customers
INNER JOIN Orders
ON Customers.first_name = Orders.customer_id;
--JOIN customer first name with customer id?


SELECT item,
  CASE quantity
    WHEN quantity < 10 THEN 'Low'
    WHEN quantity < 20 THEN 'Medium'
    ELSE 'High'
  END AS category
FROM Products;
--DO NOT USE CASE QUANTITY, ITS BEING CALLED IN WHEN STATEMENTS
