SELECT 
    CASE
        WHEN g.grade >= 8 THEN S.Name 
        ELSE "NULL" 
    END AS name,
    g.grade,
    s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.grade DESC, s.Name, s.Marks