SELECT 
    airline_name,
    flight_number,
    departure_airport,
    departure_date,
    departure_time,
    arrival_airport,
    arrival_date,
    arrival_time,
    base_price,
    status
FROM Flight
WHERE CONCAT(departure_date, ' ', departure_time) > NOW()
ORDER BY departure_date, departure_time;

-- result:
-- mysql> SOURCE 4a.sql
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+--------------+--------------+------------+---------+
-- | airline_name | flight_number | departure_airport | departure_date | departure_time | arrival_airport | arrival_date | arrival_time | base_price | status  |
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+--------------+--------------+------------+---------+
-- | Jet Blue     |           101 | JFK               | 2025-12-15     | 08:00:00       | PVG             | 2025-12-16   | 12:00:00     |     850.00 | on-time |
-- | Jet Blue     |           103 | JFK               | 2025-12-18     | 10:30:00       | LAX             | 2025-12-18   | 13:30:00     |     350.00 | on-time |
-- | Jet Blue     |           102 | PVG               | 2025-12-20     | 14:00:00       | JFK             | 2025-12-20   | 18:00:00     |     900.00 | on-time |
-- | Jet Blue     |           104 | LAX               | 2025-12-22     | 09:00:00       | JFK             | 2025-12-22   | 17:00:00     |     380.00 | delayed |
-- | Jet Blue     |           105 | JFK               | 2025-12-25     | 15:00:00       | PVG             | 2025-12-26   | 19:00:00     |     920.00 | delayed |
-- +--------------+---------------+-------------------+----------------+----------------+-----------------+--------------+--------------+------------+---------+
-- 5 rows in set (0.001 sec)