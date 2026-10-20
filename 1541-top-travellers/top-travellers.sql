# Write your MySQL query statement below
SELECT
  Users.name,
  IFNULL(SUM(Rides.distance), 0) AS travelled_distance
