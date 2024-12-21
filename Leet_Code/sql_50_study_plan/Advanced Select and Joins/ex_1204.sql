SELECT person_name
FROM (
    SELECT *, SUM(weight) OVER (ORDER BY turn) as weight_cum 
    FROM Queue
) as subquery_alias
WHERE weight_cum <= 1000
ORDER BY weight_cum DESC LIMIT 1