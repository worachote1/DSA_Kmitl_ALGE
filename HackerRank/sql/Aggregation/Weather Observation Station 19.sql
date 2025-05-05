/*
Enter your query here.
*/
SELECT
    ROUND(SQRT(POW(MIN(s.LAT_N)-MAX(s.LAT_N), 2) + POW(MIN(s.LONG_W)-MAX(s.LONG_W), 2)), 4)
FROM STATION s