/*
Enter your query here.
*/
SELECT 
    ROUND(SUM(s.LAT_N),2),
    ROUND(SUM(s.LONG_W),2)
FROM STATION s