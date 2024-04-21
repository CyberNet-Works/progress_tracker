SELECT title
FROM BOOKS
WHERE title LIKE '% %' AND title NOT LIKE '%Z%'
ORDER BY title ASC;

/*
Challenge:
Books With Multiple Words But No 'Z'
Medium
Problem Description
Suppose you have the following table:

Table - Books

id	title	release_date	publisher
1	Homo Deus	2018	Harper Collins
2	Kaizen	2019	Blue Bird
3	Animal Farm	1945	Penguin
Task: Retrieve the titles of all books that have more than one word in their title, but none of the words contain the letter Z. Order the book titles in ascending order.

Expected Result

title
Animal Farm
Homo Deus

*/