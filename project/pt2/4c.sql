SELECT DISTINCT 
    c.name,
    c.customer_email
FROM Customer c
JOIN Ticket t ON c.customer_email = t.customer_email
ORDER BY c.name;

-- mysql> SOURCE 4c.sql
-- +------------+----------------------+
-- | name       | customer_email       |
-- +------------+----------------------+
-- | Bob Zhang  | bob.zhang@email.com  |
-- | Jane Smith | jane.smith@email.com |
-- | John Doe   | john.doe@email.com   |
-- +------------+----------------------+
-- 3 rows in set (0.003 sec)