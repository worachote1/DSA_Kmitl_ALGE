/*
Enter your query here.
*/
SELECT
    e.months * e.salary AS total_earnings,
    COUNT(*)
FROM Employee e
GROUP BY total_earnings
HAVING total_earnings = (
    SELECT 
        MAX(e1.months * e1.salary)
    FROM Employee e1
)