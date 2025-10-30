SELECT 
    airline_name,
    flight_number,
    departure_airport,
    departure_date,
    departure_time,
    arrival_airport,
    status
FROM Flight
WHERE status = 'delayed'
ORDER BY departure_date, departure_time;

-- mysql> SOURCE 4b.sql
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+---------+
-- | airline_name | flight_number | departure_airport | departure_date | departure_time | arrival_airport | status  |
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+---------+
-- | Jet Blue     |           104 | LAX               | 2025-12-22     | 09:00:00       | JFK             | delayed |
-- | Jet Blue     |           105 | JFK               | 2025-12-25     | 15:00:00       | PVG             | delayed |
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+---------+
-- 2 rows in set (0.001 sec)