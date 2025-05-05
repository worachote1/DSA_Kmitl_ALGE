/*
Enter your query here.
*/
SELECT 
    ROUND(MIN(s.LAT_N),4)
FROM STATION s
WHERE s.LAT_N > 38.7780