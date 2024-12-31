# Write your MySQL query statement below
SELECT DISTINCT
   MAX(e.salary) as SecondHighestSalary
FROM Employee e
WHERE e.salary < (SELECT MAX(salary) FROM Employee)