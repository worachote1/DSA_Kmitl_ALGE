/*
Enter your query here.
*/
SELECT
    ROUND(ABS(MIN(s.LAT_N) - MAX(s.LAT_N)) + ABS(MIN(s.LONG_W) - MAX(s.LONG_W)),4)
FROM STATION s