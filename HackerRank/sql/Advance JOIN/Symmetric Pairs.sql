WITH two_pair_table AS (
    SELECT
        f.X,
        f.Y,
        ROW_NUMBER() OVER (ORDER BY f.X) AS rn
    FROM Functions f
)

SELECT
    tp1.X, 
    tp1.Y
FROM two_pair_table tp1
JOIN two_pair_table tp2
    ON tp1.rn < tp2.rn
WHERE tp1.X = tp2.Y AND tp2.X = tp1.Y AND tp1.X <= tp1.Y
ORDER BY
    tp1.X