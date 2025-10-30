SELECT 
    airline_name,
    id_number,
    num_seats,
    manufacturer,
    age
FROM Airplane
WHERE airline_name = 'Jet Blue'
ORDER BY id_number;

-- mysql> SOURCE 4d.sql
-- +--------------+-----------+-----------+--------------+-----+
-- | airline_name | id_number | num_seats | manufacturer | age |
-- +--------------+-----------+-----------+--------------+-----+
-- | Jet Blue     |         1 |       200 | Boeing       |   5 |
-- | Jet Blue     |         2 |       180 | Airbus       |   3 |
-- | Jet Blue     |         3 |       220 | Boeing       |   7 |
-- +--------------+-----------+-----------+--------------+-----+
-- 3 rows in set (0.002 sec)