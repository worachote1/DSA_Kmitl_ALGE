# Write your MySQL query statement below
WITH 
cte_count_requester AS (
    SELECT 
        requester_id as id, 
        count(accepter_id) as count_req_or_acc
    FROM RequestAccepted
    GROUP BY requester_id
),
cte_count_accepter AS (
    SELECT 
        accepter_id as id, 
        count(requester_id) as count_req_or_acc
    FROM RequestAccepted
    GROUP BY accepter_id
)

SELECT id, SUM(count_req_or_acc) as num
FROM (
    SELECT * FROM cte_count_requester
    UNION ALL
    SELECT * FROM cte_count_accepter
) temp_table
GROUP BY id
ORDER BY num DESC
LIMIT 1