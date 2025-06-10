SELECT COUNT(*)
FROM customer c
WHERE c.birthdate BETWEEN '1932-01-01' AND '1937-12-31'; -- convert to Gregorian calendar dates