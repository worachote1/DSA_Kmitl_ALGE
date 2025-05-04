    temp_table.hacker_id AS hacker_id,
    temp_table.name AS name,
    SUM(temp_table.max_score_by_user_challenge) AS total_score
FROM (
    SELECT
        h.hacker_id,
        h.name,
        MAX(s.score) AS max_score_by_user_challenge
    FROM Hackers h
    JOIN Submissions s
        ON h.hacker_id = s.hacker_id
    GROUP BY h.hacker_id, h.name, s.challenge_id
) temp_table
GROUP BY hacker_id, name
HAVING total_score != 0
ORDER BY 
    total_score DESC,
    temp_table.hacker_id