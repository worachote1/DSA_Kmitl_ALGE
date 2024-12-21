# Write your MySQL query statement below
SELECT DISTINCT L1.num as ConsecutiveNums
FROM Logs as L1
INNER JOIN Logs L2 
    ON L1.id = L2.id-1 AND L1.num = L2.num
INNER JOIN Logs L3
    ON L2.id = L3.id-1 AND L2.num = L3.num