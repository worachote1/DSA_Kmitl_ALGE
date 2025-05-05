/*
Enter your query here.
*/
SELECT CEIL(AVG(e.Salary) - AVG(REPLACE(Salary,'0','')))
FROM EMPLOYEES e