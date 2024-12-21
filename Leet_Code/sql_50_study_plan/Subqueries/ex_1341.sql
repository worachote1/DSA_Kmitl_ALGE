# Write your MySQL query statement below
SELECT name AS results 
FROM(
    SELECT 
        u1.name, 
        COUNT(mr1.rating) OVER (PARTITION BY mr1.user_id) as count_user_rating 
    FROM MovieRating mr1
    LEFT JOIN Users u1 ON mr1.user_id = u1.user_id
    ORDER BY count_user_rating DESC, u1.name ASC LIMIT 1
) temp_user_table

UNION ALL

SELECT title AS results 
FROM(
    SELECT 
        m1.title,
        AVG(mr1.rating) OVER (PARTITION BY mr1.movie_id) as avg_movie_rating 
    FROM MovieRating mr1
    LEFT JOIN Movies m1 ON mr1.movie_id = m1.movie_id
    WHERE YEAR(mr1.created_at) = 2020 AND MONTH(mr1.created_at) = 2
    ORDER BY avg_movie_rating  DESC, m1.title ASC LIMIT 1
) temp_movie_table