-- Number by score
SELECT score, COUNT(*) AS Number
FROM second_table
GROUP BY Score
ORDER BY number DESC;