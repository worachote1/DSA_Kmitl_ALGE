# Write your MySQL query statement below
SELECT 
    SUBSTR(t.trans_date, 1, 7) as month, 
    t.country, 
    count(t.id) as trans_count, 
    SUM(IF(t.state = 'approved', 1, 0)) as approved_count,
    SUM(t.amount) as trans_total_amount,
    SUM(IF(t.state = 'approved', t.amount, 0)) as approved_total_amount
FROM Transactions t
GROUP BY month, t.country