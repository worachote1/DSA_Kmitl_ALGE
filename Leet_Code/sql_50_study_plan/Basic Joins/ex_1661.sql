# Write your MySQL query statement below
SELECT temp_1.machine_id, ROUND(AVG(temp_1.timestamp - temp_2.timestamp), 3) as processing_time FROM Activity temp_1
JOIN Activity temp_2
ON (temp_1.machine_id = temp_2.machine_id ) AND 
    (temp_1.process_id = temp_2.process_id ) AND 
    (temp_1.activity_type = 'end' AND temp_2.activity_type = 'start') 
GROUP BY temp_1.machine_id