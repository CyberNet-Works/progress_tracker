SELECT
    candidate_id,
    name
        AS fit_candidate

FROM Candidates
WHERE python = 'Good' AND SQL = 'Good'

ORDER BY 
    candidate_id ASC
;

/*
Sort the Candidates in Ascending Order
Medium
Problem Description
Consider the following table:

Table - Candidates

candidate_id	name	python	SQL
1	Harry	Good	Good
2	Dennis	Poor	Decent
3	Wayne	Good	Poor
4	Ryan	Good	Good
5	Darren	Good	Good
Task: Retrieve the candidates suitable for a job in data science under the alias fit_candidate and sort the result in ascending order of candidate_id.

Assumption: A candidate is suitable for the job if they are Good at both python and SQL.

Expected Result

candidate_id	fit_candidate
1	Harry
4	Ryan
5	Darren

*/