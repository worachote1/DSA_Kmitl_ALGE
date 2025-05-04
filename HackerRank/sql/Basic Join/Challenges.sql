SELECT 
    h.hacker_id, 
    h.name,
    COUNT(c.challenge_id)AS total_cnt
FROM Hackers h
JOIN Challenges c
    ON h.hacker_id = c.hacker_id
    
GROUP BY h.hacker_id, h.name

HAVING total_cnt = (
    SELECT COUNT(c1.hacker_id) AS max_cnt 
    FROM Challenges c1 
    GROUP BY c1.hacker_id
    ORDER BY max_cnt DESC
    LIMIT 1
) OR total_cnt IN (
    SELECT temp_count FROM (
        SELECT COUNT(c2.hacker_id) as temp_count
        FROM Challenges c2 
        GROUP BY c2.hacker_id
    ) temp_table
    GROUP BY temp_count
    HAVING COUNT(temp_count) = 1 
)

ORDER BY
    total_cnt DESC,
    h.hacker_id