-- for now i use MS SQL Server
WITH sub_with_nday_nhacker AS (
    SELECT
        sub.submission_date AS submission_date,
        sub.hacker_id AS hacker_id,
        DENSE_RANK() OVER(ORDER BY sub.submission_date) AS nday,
        DENSE_RANK() OVER(PARTITION BY sub.hacker_id ORDER BY sub.submission_date) AS nhacker,
        COUNT(*) AS cnt_sub_by_day_hacker
    FROM Submissions sub
    GROUP BY submission_date, hacker_id
),
sub_summary AS (
    SELECT
        sb_w.submission_date AS submission_date,
        sb_w.hacker_id AS hacker_id, 
        SUM(CASE WHEN sb_w.nday = sb_w.nhacker THEN 1 ELSE 0 END) OVER(PARTITION BY sb_w.submission_date) AS total_unique_hacker,
        DENSE_RANK() OVER(PARTITION BY sb_w.submission_date ORDER BY sb_w.cnt_sub_by_day_hacker DESC, sb_w.hacker_id) AS rank_hacker
    FROM sub_with_nday_nhacker sb_w
)

SELECT
    sb_s.submission_date AS submission_date,
    sb_s.total_unique_hacker AS total_unique_hacker,
    h.hacker_id AS hacker_id,
    h.name AS name 
FROM sub_summary sb_s
JOIN Hackers h
    ON sb_s.hacker_id = h.hacker_id
WHERE sb_s.rank_hacker = 1