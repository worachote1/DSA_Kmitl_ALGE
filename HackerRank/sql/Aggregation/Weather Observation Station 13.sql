/*
Enter your query here.
*/
SELECT 
    ROUND(SUM(s.LAT_N),4)
FROM STATION s
WHERE s.LAT_N > 38.7880 AND s.LAT_N < 137.2345