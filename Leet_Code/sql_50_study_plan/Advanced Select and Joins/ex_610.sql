# Write your MySQL query statement below
SELECT x, y, z, IF(x+y+z-GREATEST(x,y,z) > GREATEST(x,y,z), 'Yes', 'No') as triangle
FROM Triangle