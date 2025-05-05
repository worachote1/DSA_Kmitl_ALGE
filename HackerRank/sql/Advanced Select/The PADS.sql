/*
Enter your query here.
*/
SELECT 
    CONCAT(o.name, '(', SUBSTRING(o.Occupation, 1, 1), ')')
FROM OCCUPATIONS o
ORDER BY
    o.name;

SELECT
    CONCAT('There are a total of ', COUNT(*), ' ', LOWER(o1.Occupation), 's.')
FROM OCCUPATIONS o1
GROUP BY o1.Occupation
ORDER BY
    COUNT(*),
    o1.Occupation;
