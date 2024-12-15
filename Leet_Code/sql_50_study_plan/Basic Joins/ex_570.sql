# Write your MySQL query statement below
SELECT em2.name
FROM Employee em1
LEFT JOIN Employee em2 ON em1.managerId = em2.id
GROUP BY em2.id
HAVING COUNT(em2.id) >= 5