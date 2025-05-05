/*
Enter your query here.
*/

SELECT 
    MAX(CASE WHEN temp_table.Occupation = 'Doctor' THEN temp_table.Name END),
    MAX(CASE WHEN temp_table.Occupation = 'Professor' THEN temp_table.Name END),
    MAX(CASE WHEN temp_table.Occupation = 'Singer' THEN temp_table.Name END),
    MAX(CASE WHEN temp_table.Occupation = 'Actor' THEN temp_table.Name END)
FROM (
    SELECT 
        o.Name AS Name,
        o.Occupation AS Occupation,
        ROW_NUMBER() OVER (
            PARTITION BY o.Occupation
            ORDER BY NAME
        ) AS row_number_by_occ
    FROM OCCUPATIONS o
) temp_table
GROUP BY temp_table.row_number_by_occ