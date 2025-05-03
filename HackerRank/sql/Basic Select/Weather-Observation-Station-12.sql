SELECT DISTINCT s.CITY 
FROM STATION s 
WHERE LEFT(s.CITY, 1) NOT IN ('a','e','i','o','u') AND
      RIGHT(s.CITY, 1) NOT IN ('a','e','i','o','u')