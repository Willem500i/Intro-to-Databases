-- Test Scenario Data for Demo (12/10/2025 and 12/11/2025)
-- IMPORTANT: Backup your existing data before running this script
-- This script will DELETE all existing data and load test scenario data

-- Clear existing data (in reverse order of dependencies)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Review;
TRUNCATE TABLE Ticket;
TRUNCATE TABLE Phone;
TRUNCATE TABLE AirlineStaff;
TRUNCATE TABLE Customer;
TRUNCATE TABLE Flight;
TRUNCATE TABLE Airplane;
TRUNCATE TABLE Airport;
TRUNCATE TABLE Airline;
SET FOREIGN_KEY_CHECKS = 1;

-- Add Airline
INSERT INTO Airline (name) VALUES ('United');

-- Add Airline Staff
INSERT INTO AirlineStaff (username, password, name_first, name_last, date_of_birth, airline_name, email) VALUES
('admin', MD5('abcd'), 'Roe', 'Jones', '1978-05-25', 'United', 'staff@nyu.edu');

-- Add Phone numbers for staff
INSERT INTO Phone (staff_username, phone_number) VALUES
('admin', '111-2222-3333'),
('admin', '444-5555-6666');

-- Add Airplanes
INSERT INTO Airplane (airline_name, id_number, num_seats, manufacturer, age) VALUES
('United', 1, 4, 'Boeing', 10),
('United', 2, 4, 'Airbus', 12),
('United', 3, 50, 'Boeing', 8);

-- Add Airports
INSERT INTO Airport (airport_code, city, country, airport_type) VALUES
('JFK', 'NYC', 'USA', 'both'),
('BOS', 'Boston', 'USA', 'both'),
('PVG', 'Shanghai', 'China', 'both'),
('BEI', 'Beijing', 'China', 'both'),
('SFO', 'San Francisco', 'USA', 'both'),
('LAX', 'Los Angeles', 'USA', 'both'),
('HKA', 'Hong Kong', 'China', 'both'),
('SHEN', 'Shenzhen', 'China', 'both');

-- Add Customers
INSERT INTO Customer (customer_email, name, password, building_number, street, city, state, 
                     phone_number, passport_number, passport_expiration, passport_country, date_of_birth) VALUES
('testcustomer@nyu.edu', 'Jon Snow', MD5('1234'), 1555, 'Jay St', 'Brooklyn', 'New York', 
 '123-4321-4321', '54321', '2025-12-24', 'USA', '1999-12-19'),
('user1@nyu.edu', 'Alice Bob', MD5('1234'), 5405, 'Jay Street', 'Brooklyn', 'New York', 
 '123-4322-4322', '54322', '2025-12-25', 'USA', '1999-11-19'),
('user3@nyu.edu', 'Trudy Jones', MD5('1234'), 1890, 'Jay Street', 'Brooklyn', 'New York', 
 '123-4324-4324', '54324', '2025-09-24', 'USA', '1999-09-19');

-- Add Flights
INSERT INTO Flight (airline_name, flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, status, airplane_id) VALUES
('United', 102, 'SFO', '2025-09-14', '13:25:25', 'LAX', '2025-09-14', '16:50:25', 300.00, 'on-time', 3),
('United', 104, 'PVG', '2025-10-14', '13:25:25', 'BEI', '2025-10-14', '16:50:25', 300.00, 'on-time', 3),
('United', 206, 'SFO', '2026-01-04', '13:25:25', 'LAX', '2026-01-04', '16:50:25', 350.00, 'on-time', 2),
('United', 207, 'LAX', '2026-02-05', '13:25:25', 'SFO', '2026-02-05', '16:50:25', 300.00, 'on-time', 2),
('United', 296, 'PVG', '2025-12-28', '13:25:25', 'SFO', '2025-12-28', '16:50:25', 3000.00, 'on-time', 1),
('United', 715, 'PVG', '2025-09-25', '10:25:25', 'BEI', '2025-09-25', '13:50:25', 500.00, 'delayed', 1);

-- Add Tickets with specific ticket IDs and purchase information
-- Note: We need to manually set ticket_id since AUTO_INCREMENT would normally handle this
-- We'll insert with explicit ticket_id values

INSERT INTO Ticket (ticket_id, customer_email, flight_airline, flight_number, 
                   flight_departure_date, flight_departure_time,
                   card_type, card_number, card_name, card_expiry, 
                   purchase_date, purchase_time) VALUES
(1, 'testcustomer@nyu.edu', 'United', 102, '2025-09-14', '13:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2026-03-01', '2025-08-15', '11:55:55'),
(2, 'user1@nyu.edu', 'United', 102, '2025-09-14', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 1', '2026-03-01', '2025-08-20', '11:55:55'),
(3, 'user1@nyu.edu', 'United', 104, '2025-10-14', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 1', '2026-03-01', '2025-09-21', '11:55:55'),
(4, 'testcustomer@nyu.edu', 'United', 104, '2025-10-14', '13:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2027-03-01', '2025-09-28', '11:55:55'),
(5, 'user3@nyu.edu', 'United', 102, '2025-09-14', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 3', '2026-03-01', '2025-07-16', '11:55:55'),
(6, 'testcustomer@nyu.edu', 'United', 715, '2025-09-25', '10:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2026-03-01', '2024-09-20', '11:55:55'),
(7, 'user3@nyu.edu', 'United', 206, '2026-01-04', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 3', '2026-03-01', '2025-11-20', '11:55:55'),
(8, 'user1@nyu.edu', 'United', 206, '2026-01-04', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 1', '2026-03-01', '2025-10-21', '11:55:55'),
(9, 'user1@nyu.edu', 'United', 207, '2026-02-05', '13:25:25', 
 'credit', '1111-2222-3333-5555', 'User 1', '2026-03-01', '2025-12-02', '11:55:55'),
(10, 'testcustomer@nyu.edu', 'United', 207, '2026-02-05', '13:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2026-03-01', '2025-10-25', '11:55:55'),
(11, 'user1@nyu.edu', 'United', 296, '2025-12-28', '13:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2026-03-01', '2025-10-22', '11:55:55'),
(12, 'testcustomer@nyu.edu', 'United', 296, '2025-12-28', '13:25:25', 
 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2026-03-01', '2025-11-20', '11:55:55');

-- Reset AUTO_INCREMENT to continue from 13 after manual inserts
ALTER TABLE Ticket AUTO_INCREMENT = 13;

-- Add Reviews
INSERT INTO Review (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   rating, comment) VALUES
('testcustomer@nyu.edu', 'United', 102, '2025-09-14', '13:25:25', 
 4, 'Very Comfortable'),
('user1@nyu.edu', 'United', 102, '2025-09-14', '13:25:25', 
 5, 'Relaxing, check-in and onboarding very professional'),
('testcustomer@nyu.edu', 'United', 104, '2025-10-14', '13:25:25', 
 1, 'Customer Care services are not good'),
('user1@nyu.edu', 'United', 104, '2025-10-14', '13:25:25', 
 5, 'Comfortable journey and Professional');

