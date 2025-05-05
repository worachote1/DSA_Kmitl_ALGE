/*
Enter your query here.
*/
SELECT
    ROUND(temp_table.LAT_N, 4)
FROM (
    SELECT 
        LAT_N,
        ROW_NUMBER() OVER(ORDER BY s.LAT_N) AS row_index
    FROM STATION s
) temp_table
WHERE temp_table.row_index = ((
    SELECT COUNT(*) FROM STATION
) + 1) / 2