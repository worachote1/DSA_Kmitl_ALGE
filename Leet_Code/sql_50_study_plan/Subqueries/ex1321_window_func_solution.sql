SELECT DISTINCT
    visited_on, 
    sum_day_window as amount, 
    ROUND(sum_day_window/7, 2) as average_amount
FROM (
    SELECT 
        c.visited_on,
        SUM(c.amount) OVER(ORDER BY c.visited_on RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW) as sum_day_window
    FROM Customer c
) result_table
WHERE DATE_SUB(visited_on, INTERVAL 6 DAY) IN (SELECT visited_on FROM Customer)