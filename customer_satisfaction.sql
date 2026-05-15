SELECT "Ticket Priority", AVG("Customer Satisfaction Rating")
FROM tickets
GROUP BY "Ticket Priority";