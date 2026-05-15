SELECT 
CASE 
  WHEN "Customer Age" < 25 THEN '18-24'
  WHEN "Customer Age" < 35 THEN '25-34'
  WHEN "Customer Age" < 50 THEN '35-49'
  ELSE '50+'
END AS age_group,
COUNT(*)
FROM tickets
GROUP BY age_group;