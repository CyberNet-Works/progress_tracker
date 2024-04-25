--strftime_weekeneds
SELECT *
FROM Shows
WHERE STRFTIME('%w', air_date) NOT IN ('0', '6')
ORDER BY rating DESC
LIMIT 1;


/*
Challenge:
Highest Rated Episode
Hard
Problem Description
Consider the following table:

Table - Shows

show_id	title	episode_name	air_date	rating
1	FRIENDS	The One with the Rumor	2023-05-1	7
2	GOT	Baelor	2023-05-08	8
3	HIMYM	Slap Bet	2023-05-11	9
4	GOT	The Rains of Castamere	2023-05-14	10
Task: Retrieve the details of the highest-rated episode but exclude any episode that aired on weekends.

Assumption: Consider Saturday and Sunday as weekends.

Expected Result

show_id	title	episode_name	air_date	rating
3	HIMYM	Slap Bet	2023-05-11	9
*/