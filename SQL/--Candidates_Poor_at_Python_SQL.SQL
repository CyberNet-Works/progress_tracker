--Candidates_Poor_at_Python_SQL.SQL
SELECT 
    candidate_id,
    name as unfit_candidate
FROM Candidates
WHERE 
    python = 'Poor' OR SQL = 'Poor'
ORDER BY candidate_id ASC;



/*
Candidates Poor at Python and SQL
Medium
Problem Description
Suppose we have the following table:

Table - Candidates

candidate_id	name	python	SQL
1	Harry	Good	Good
2	Dennis	Poor	Decent
3	Wayne	Good	Poor
4	Ryan	Good	Good
5	Darren	Good	Good
Task: Find the candidates unsuitable for data science job under the unfit_candidate alias. They must be Poor at either python or SQL. Sort the output in ascending order of candidate_id.

Expected Result

candidate_id	unfit_candidate
2	Dennis 
3	Wayne

*/
