SELECT
    CASE
        WHEN "Time to Resolution" <= 24 THEN 'Fast'
        WHEN "Time to Resolution" <= 48 THEN 'Moderate'
        ELSE 'Slow'
    END AS resolution_bucket,

    ROUND(AVG("Customer Satisfaction Rating"), 2) AS avg_satisfaction,
    COUNT(*) AS total_tickets

FROM tickets
GROUP BY resolution_bucket
ORDER BY avg_satisfaction DESC;
