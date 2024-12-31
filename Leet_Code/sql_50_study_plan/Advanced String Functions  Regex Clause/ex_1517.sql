# Write your MySQL query statement below
SELECT * 
FROM Users u
WHERE u.mail REGEXP '^[A-Za-z][A-Za-z0-9_./-]*@leetcode[.]com$'