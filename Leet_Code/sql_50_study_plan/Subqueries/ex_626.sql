# Write your MySQL query statement below
SELECT IF(s.id = (SELECT MAX(id) FROM Seat) AND s.id % 2 != 0 , s.id,
    IF(s.id % 2 = 0, s.id - 1, s.id + 1)
) as id, student
FROM Seat s
ORDER BY id