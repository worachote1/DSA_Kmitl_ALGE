SELECT DISTINCT s.CITY 
FROM STATION s 
WHERE LEFT(s.CITY, 1) NOT IN ('a','e','i','o','u') OR
      RIGHT(s.CITY, 1) NOT IN ('a','e','i','o','u')