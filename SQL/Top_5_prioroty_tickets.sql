WITH high_priority_tickets AS (
    SELECT *
    FROM tickets
    WHERE "Ticket Priority" = 'High'
)

SELECT
    "Product Purchased",
    COUNT(*) AS total_high_priority_tickets
FROM high_priority_tickets
GROUP BY "Product Purchased"
ORDER BY total_high_priority_tickets DESC
LIMIT 5;
