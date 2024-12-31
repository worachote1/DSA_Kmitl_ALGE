SELECT
    ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM (
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY lat,lon) as count_lat_lon,
        COUNT(*) OVER(PARTITION BY tiv_2015) as count_tiv_2015
    FROM Insurance
) temp
WHERE count_lat_lon = 1 AND count_tiv_2015 > 1