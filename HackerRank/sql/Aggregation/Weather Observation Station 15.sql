/*
Enter your query here.
*/
SELECT 
    ROUND(s.LONG_W,4)
FROM STATION s
WHERE s.LAT_N = (
    SELECT MAX(s1.LAT_N)
    FROM STATION s1
    WHERE s1.LAT_N < 137.2345
)