--! SQL
--Highest_Rated_Anime_Titles.SQL

SELECT title
FROM Anime
WHERE 
    seasons > 1 AND
    rating > (SELECT AVG(rating) FROM Anime); 

/*

Highest Rated Anime Titles
Medium
Problem Description
Consider the following table:

Table - Anime

id	title	rating	seasons
1	Dragon Ball	10	20
2	One Piece	9	23
3	Death Note	10	1
4	My Hero Academia	7	6
5	Assassination Classroom	6	2
Task: Retrieve the names of all anime titles with more than one season and rating greater than the average rating of the table.

Expected Result

title
Dragon Ball
One Piece
*/
