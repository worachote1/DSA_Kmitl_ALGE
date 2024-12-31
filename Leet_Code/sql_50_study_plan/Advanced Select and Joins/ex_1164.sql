# Write your MySQL query statement below
SELECT
    DISTINCT p2.product_id,
    IF(p1.new_price IS NOT NULL, p1.new_price, 10) as price
FROM
(
    SELECT *
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date) as change_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) p1
RIGHT JOIN Products p2
ON p1.product_id = p2.product_id


-- CTE solution

-- # Write your MySQL query statement below
-- WITH cte_product AS (
--     SELECT         
--         DISTINCT product_id,
--         new_price as price
--     FROM Products
--     WHERE (product_id, change_date) IN (
--         SELECT product_id, MAX(change_date) as change_date
--         FROM Products
--         WHERE change_date <= '2019-08-16'
--         GROUP BY product_id
--     )
-- )

-- SELECT * FROM cte_product

-- UNION

-- SELECT 
--     DISTINCT product_id,
--     10 as price
-- FROM Products
-- WHERE change_date > '2019-08-16' AND (product_id) NOT IN (SELECT product_id FROM cte_product)