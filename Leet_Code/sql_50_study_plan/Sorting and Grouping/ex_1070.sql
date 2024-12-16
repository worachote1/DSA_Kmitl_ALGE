# Write your MySQL query statement below
SELECT s.product_id, s.year as first_year, s.quantity, s.price
FROM Sales s WHERE (s.product_id, year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
)