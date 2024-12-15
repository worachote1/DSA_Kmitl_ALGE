# Write your MySQL query statement below
SELECT st.student_id, st.student_name, sub.subject_name, COUNT(ex.student_id) as attended_exams
FROM Students st
CROSS JOIN Subjects sub
LEFT JOIN Examinations ex ON (st.student_id = ex.student_id) AND (sub.subject_name = ex.subject_name)
GROUP BY st.student_id, st.student_name, sub.subject_name
ORDER BY st.student_id, st.student_name