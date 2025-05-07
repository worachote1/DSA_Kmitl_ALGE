SELECT
    con.contest_id,
    con.hacker_id,
    con.name,
    sum_ss.sum_total_submissions,
    sum_ss.sum_total_accepted_submissions,
    sum_vs.sum_total_views,
    sum_vs.sum_total_unique_views
FROM Contests con

JOIN (
    SELECT
        col.contest_id AS contest_id,
        SUM(total_submissions) AS sum_total_submissions,
        SUM(total_accepted_submissions) AS sum_total_accepted_submissions
    FROM Colleges col
    JOIN Challenges cha ON col.college_id = cha.college_id
    JOIN Submission_Stats ss ON cha.challenge_id = ss.challenge_id
    GROUP BY col.contest_id
) sum_ss
ON con.contest_id = sum_ss.contest_id

JOIN (
    SELECT
        col.contest_id AS contest_id,
        SUM(total_views) AS sum_total_views,
        SUM(total_unique_views) AS sum_total_unique_views
    FROM Colleges col
    JOIN Challenges cha ON col.college_id = cha.college_id
    JOIN View_Stats vs ON cha.challenge_id = vs.challenge_id
    GROUP BY col.contest_id
) sum_vs 
ON con.contest_id = sum_vs.contest_id

WHERE sum_ss.sum_total_submissions > 0 AND 
      sum_ss.sum_total_accepted_submissions > 0 AND 
      sum_vs.sum_total_views > 0 AND
      sum_vs.sum_total_unique_views > 0

ORDER BY con.contest_id