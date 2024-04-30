--! SQL

-- Books_That_Contain_Z_in_Title.SQL

SELECT title
FROM Books
WHERE 
    SUBSTR(release_date,1,2) = '20' AND
    LOWER(title) LIKE '%z%'; 

/*
Books That Contain Z on Its Title
Medium
Problem Description
Consider the following table:

Table - Books

id	title	release_date	publisher
1	Homo Deus	2018	Harper Collins
2	Kaizen	2019	Blue Bird
3	Animal Farm	1945	Penguin
Task: Retrieve the titles of all books published in the 21st century that contain the letter Z.

Expected Result

title
Kaizen
*/
