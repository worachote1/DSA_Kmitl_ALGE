# Write your MySQL query statement below
SELECT DISTINCT
    visited_on,
    amount_7_days_window as amount,
    ROUND(amount_7_days_window / 7, 2) as average_amount
FROM (
    SELECT 
        c1.visited_on ,
        (
            SELECT SUM(c2.amount)  FROM Customer c2
            WHERE c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
        )as amount_7_days_window
    FROM Customer c1
) temp1
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    FROM Customer
)
ORDER BY visited_on