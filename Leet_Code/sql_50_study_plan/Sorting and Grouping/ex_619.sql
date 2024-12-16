# Write your MySQL query statement below
SELECT MAX(mn.num) as num
FROM MyNumbers mn WHERE (mn.num) IN (
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING(COUNT(num) = 1)
)
