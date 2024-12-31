# Write your MySQL query statement below
SELECT
    ROUND(SUM(I1.tiv_2016), 2) as tiv_2016
FROM Insurance I1
WHERE (I1.tiv_2015) IN (
    SELECT 
        I2.tiv_2015
    FROM Insurance I2 
    WHERE I2.pid != I1.pid AND I2.tiv_2015 = I1.tiv_2015

) AND (I1.lat, I1.lon) NOT IN (
    SELECT 
        I2.lat, I2.lon
    FROM Insurance I2 
    WHERE I2.pid != I1.pid AND I2.lat = I1.lat AND I2.lon = I1.lon
)