--! SQL
--check_consecutive_days.sql
WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_login_date
  FROM Games
  GROUP BY player_id
),
consecutive_logins AS (
  SELECT player_id, COUNT(*) AS consecutive_days
  FROM (
    SELECT player_id, event_date,
           DATE(event_date, '+1 day') AS next_day,
     LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS next_login
    FROM Games
  ) 
  WHERE next_day = next_login
  GROUP BY player_id
)
SELECT ROUND(CAST(COUNT(DISTINCT player_id) AS REAL) / (SELECT COUNT(DISTINCT player_id) FROM Games), 2) AS login_fraction
FROM consecutive_logins;

/*

!! Very difficult, got assistance

Challenge:
Gameplay Analysis
Hard
Problem Description
Consider the following table:

Table - Games

player_id	device_id	event_date	games_played
1	2	2023-05-01	5
1	2	2023-05-02	6
2	3	2023-07-20	1
3	1	2023-08-06	0
3	4	2023-09-01	5
Task: Retrieve the fraction of players that logged in again on the day after they first logged in, rounded to 2 decimal places.

Hint: You need to count the number of players logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

Expected Result

login_fraction
0.33
*/