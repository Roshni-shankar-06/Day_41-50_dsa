# Write your MySQL query statement below
SELECT 
    patient_id, 
    patient_name, 
    conditions
FROM 
    Patients
WHERE 
    conditions LIKE 'DIAB1%'      -- Matches if DIAB1 is the first condition
    OR conditions LIKE '% DIAB1%'; -- Matches if DIAB1 follows a space
