-- Number by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY Score
ORDER BY number DESC;