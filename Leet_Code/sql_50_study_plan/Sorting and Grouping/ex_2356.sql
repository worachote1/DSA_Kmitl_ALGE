# Write your MySQL query statement below
SELECT t.teacher_id, COUNT(DISTINCT subject_id) as cnt
FROM Teacher t
GROUP BY t.teacher_id