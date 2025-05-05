/*
Enter your query here.
*/
SELECT
    b.N,
    (
    CASE
        WHEN b.P IS NULL THEN 'Root'
        WHEN b.N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END
    ) AS node_type
FROM BST b
ORDER BY
    b.N