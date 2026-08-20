SELECT "Ticket Type", COUNT(*) AS total
FROM tickets
GROUP BY "Ticket Type"
ORDER BY total DESC;
