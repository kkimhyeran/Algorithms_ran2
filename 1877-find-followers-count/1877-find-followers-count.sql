/* Write your PL/SQL query statement below */


SELECT user_id , count(*) as followers_count
FROM Followers 
GROUP BY user_id 
ORDER BY user_id