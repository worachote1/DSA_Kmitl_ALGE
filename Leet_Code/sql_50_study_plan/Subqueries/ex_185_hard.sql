# Write your MySQL query statement below
SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) as dense_rank_salary_by_dep
    FROM Employee e
    INNER JOIN Department d
    ON e.departmentId = d.id
) temp
WHERE dense_rank_salary_by_dep <= 3