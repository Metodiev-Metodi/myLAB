SELECT
    "Ticket Channel",

    ROUND(
        AVG("Customer Satisfaction Rating") /
        AVG("Time to Resolution"),
        4
    ) AS efficiency_score

FROM tickets
GROUP BY "Ticket Channel"
ORDER BY efficiency_score DESC;
