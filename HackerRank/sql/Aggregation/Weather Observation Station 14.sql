/*
Enter your query here.
*/
SELECT 
    ROUND(MAX(s.LAT_N),4)
FROM STATION s
WHERE s.LAT_N < 137.2345