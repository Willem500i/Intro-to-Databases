-- Insert Airlines
INSERT INTO Airline (name) VALUES 
('Jet Blue'),
('American Airlines'),
('Delta Air Lines'),
('United Airlines');

-- Insert Airports (10 total airports)
INSERT INTO Airport (airport_code, city, country, airport_type) VALUES
('JFK', 'New York City', 'USA', 'international'),
('PVG', 'Shanghai', 'China', 'international'),
('LAX', 'Los Angeles', 'USA', 'international'),
('ORD', 'Chicago', 'USA', 'both'),
('DFW', 'Dallas', 'USA', 'both'),
('LHR', 'London', 'United Kingdom', 'international'),
('CDG', 'Paris', 'France', 'international'),
('DXB', 'Dubai', 'UAE', 'international'),
('NRT', 'Tokyo', 'Japan', 'international'),
('SYD', 'Sydney', 'Australia', 'international');

-- Insert Airplanes
INSERT INTO Airplane (airline_name, id_number, num_seats, manufacturer, age) VALUES
-- Jet Blue
('Jet Blue', 1, 200, 'Boeing', 5),
('Jet Blue', 2, 180, 'Airbus', 3),
('Jet Blue', 3, 220, 'Boeing', 7),
-- American Airlines
('American Airlines', 1, 250, 'Boeing', 4),
('American Airlines', 2, 190, 'Airbus', 6),
('American Airlines', 3, 210, 'Boeing', 3),
-- Delta Air Lines
('Delta Air Lines', 1, 240, 'Boeing', 5),
('Delta Air Lines', 2, 200, 'Airbus', 4),
('Delta Air Lines', 3, 180, 'Boeing', 8),
-- United Airlines
('United Airlines', 1, 230, 'Boeing', 6),
('United Airlines', 2, 195, 'Airbus', 5),
('United Airlines', 3, 205, 'Boeing', 4);

-- Insert Customers
INSERT INTO Customer (customer_email, name, password, building_number, street, city, state, 
                     phone_number, passport_number, passport_expiration, passport_country, date_of_birth) VALUES
('john.doe@email.com', 'John Doe', MD5('password123'), 123, 'Main Street', 'New York', 'NY', 
 '212-555-0101', 'P123456', '2027-12-31', 'USA', '1990-05-15'),
('jane.smith@email.com', 'Jane Smith', MD5('securepass'), 456, 'Park Avenue', 'Los Angeles', 'CA', 
 '310-555-0202', 'P789012', '2026-06-30', 'USA', '1985-08-22'),
('bob.zhang@email.com', 'Bob Zhang', MD5('mypassword'), 789, 'Broadway', 'New York', 'NY', 
 '212-555-0303', 'P345678', '2028-03-15', 'USA', '1992-11-10'),
('alice.johnson@email.com', 'Alice Johnson', MD5('alice123'), 321, 'Oak Street', 'Chicago', 'IL', 
 '312-555-0404', 'P901234', '2027-08-20', 'USA', '1988-03-10'),
('charlie.brown@email.com', 'Charlie Brown', MD5('charlie456'), 654, 'Elm Avenue', 'Dallas', 'TX', 
 '214-555-0505', 'P567890', '2026-11-15', 'USA', '1995-07-25');

-- Insert Airline Staff
INSERT INTO AirlineStaff (username, password, name_first, name_last, date_of_birth, airline_name, email) VALUES
-- Jet Blue
('staff001', MD5('staffpass123'), 'Sarah', 'Johnson', '1988-03-20', 'Jet Blue', 'sarah.johnson@jetblue.com'),
('staff002', MD5('staffpass456'), 'Michael', 'Chen', '1990-06-15', 'Jet Blue', 'michael.chen@jetblue.com'),
-- American Airlines
('aa_staff001', MD5('staffpass123'), 'Robert', 'Williams', '1987-04-10', 'American Airlines', 'robert.williams@aa.com'),
('aa_staff002', MD5('staffpass456'), 'Lisa', 'Anderson', '1991-07-22', 'American Airlines', 'lisa.anderson@aa.com'),
-- Delta Air Lines
('delta_staff001', MD5('staffpass123'), 'David', 'Martinez', '1989-05-15', 'Delta Air Lines', 'david.martinez@delta.com'),
('delta_staff002', MD5('staffpass456'), 'Jennifer', 'Taylor', '1992-08-30', 'Delta Air Lines', 'jennifer.taylor@delta.com'),
-- United Airlines
('ua_staff001', MD5('staffpass123'), 'James', 'Brown', '1986-06-20', 'United Airlines', 'james.brown@united.com'),
('ua_staff002', MD5('staffpass456'), 'Patricia', 'Davis', '1990-09-12', 'United Airlines', 'patricia.davis@united.com');

-- Insert Phone numbers for staff
INSERT INTO Phone (staff_username, phone_number) VALUES
('staff001', '718-555-1000'),
('staff001', '718-555-1001'),
('staff002', '212-555-2000'),
('aa_staff001', '214-555-2000'),
('aa_staff002', '214-555-2001'),
('delta_staff001', '404-555-3000'),
('delta_staff002', '404-555-3001'),
('ua_staff001', '312-555-4000'),
('ua_staff002', '312-555-4001');

-- Insert Flights (spanning June 1 to December 31, 2025)
INSERT INTO Flight (airline_name, flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, status, airplane_id) VALUES
-- Jet Blue flights
('Jet Blue', 101, 'JFK', '2025-06-05', '08:00:00', 'LAX', '2025-06-05', '11:00:00', 350.00, 'on-time', 1),
('Jet Blue', 102, 'LAX', '2025-06-10', '14:00:00', 'JFK', '2025-06-10', '22:00:00', 380.00, 'on-time', 2),
('Jet Blue', 103, 'JFK', '2025-06-15', '10:30:00', 'ORD', '2025-06-15', '12:30:00', 280.00, 'on-time', 3),
('Jet Blue', 104, 'ORD', '2025-06-20', '09:00:00', 'DFW', '2025-06-20', '11:30:00', 290.00, 'delayed', 1),
('Jet Blue', 105, 'JFK', '2025-07-01', '22:00:00', 'LHR', '2025-07-02', '10:00:00', 750.00, 'on-time', 2),
('Jet Blue', 106, 'LHR', '2025-07-05', '12:00:00', 'JFK', '2025-07-05', '15:30:00', 780.00, 'on-time', 3),
('Jet Blue', 107, 'LAX', '2025-07-10', '23:30:00', 'NRT', '2025-07-11', '05:00:00', 950.00, 'on-time', 1),
('Jet Blue', 108, 'JFK', '2025-08-15', '08:00:00', 'PVG', '2025-08-16', '12:00:00', 850.00, 'on-time', 2),
('Jet Blue', 109, 'PVG', '2025-08-20', '14:00:00', 'JFK', '2025-08-21', '18:00:00', 900.00, 'delayed', 3),
('Jet Blue', 110, 'JFK', '2025-09-10', '20:00:00', 'CDG', '2025-09-11', '09:30:00', 820.00, 'on-time', 1),
('Jet Blue', 111, 'LAX', '2025-10-05', '10:00:00', 'SYD', '2025-10-06', '18:00:00', 1200.00, 'on-time', 2),
('Jet Blue', 112, 'JFK', '2025-11-15', '15:00:00', 'DXB', '2025-11-16', '12:00:00', 1100.00, 'on-time', 3),
('Jet Blue', 113, 'ORD', '2025-12-10', '11:00:00', 'LAX', '2025-12-10', '13:30:00', 320.00, 'delayed', 1),
('Jet Blue', 114, 'DFW', '2025-12-20', '07:30:00', 'JFK', '2025-12-20', '12:00:00', 310.00, 'on-time', 2),
('Jet Blue', 115, 'JFK', '2025-12-25', '08:00:00', 'LAX', '2025-12-25', '11:00:00', 400.00, 'on-time', 3),
-- American Airlines flights
('American Airlines', 201, 'JFK', '2025-06-08', '07:00:00', 'LAX', '2025-06-08', '10:00:00', 360.00, 'on-time', 1),
('American Airlines', 202, 'LAX', '2025-06-12', '15:00:00', 'ORD', '2025-06-12', '21:00:00', 330.00, 'on-time', 2),
('American Airlines', 203, 'ORD', '2025-07-05', '09:00:00', 'DFW', '2025-07-05', '11:00:00', 270.00, 'on-time', 3),
('American Airlines', 204, 'JFK', '2025-07-15', '21:00:00', 'LHR', '2025-07-16', '09:00:00', 760.00, 'delayed', 1),
('American Airlines', 205, 'LAX', '2025-08-01', '08:00:00', 'JFK', '2025-08-01', '16:00:00', 390.00, 'on-time', 2),
('American Airlines', 206, 'JFK', '2025-08-20', '10:00:00', 'CDG', '2025-08-21', '23:00:00', 830.00, 'on-time', 3),
('American Airlines', 207, 'DFW', '2025-09-10', '14:00:00', 'LAX', '2025-09-10', '16:00:00', 300.00, 'on-time', 1),
('American Airlines', 208, 'JFK', '2025-10-15', '22:00:00', 'NRT', '2025-10-16', '03:00:00', 970.00, 'delayed', 2),
('American Airlines', 209, 'ORD', '2025-11-05', '06:00:00', 'JFK', '2025-11-05', '09:00:00', 290.00, 'on-time', 3),
('American Airlines', 210, 'JFK', '2025-12-15', '11:00:00', 'PVG', '2025-12-16', '15:00:00', 870.00, 'on-time', 1),
('American Airlines', 211, 'LAX', '2025-12-22', '13:00:00', 'ORD', '2025-12-22', '19:00:00', 340.00, 'on-time', 2),
('American Airlines', 212, 'JFK', '2025-12-28', '16:00:00', 'LAX', '2025-12-28', '19:00:00', 410.00, 'delayed', 3),
-- Delta Air Lines flights
('Delta Air Lines', 301, 'JFK', '2025-06-03', '09:00:00', 'LAX', '2025-06-03', '12:00:00', 345.00, 'on-time', 1),
('Delta Air Lines', 302, 'LAX', '2025-06-18', '16:00:00', 'JFK', '2025-06-19', '00:00:00', 375.00, 'on-time', 2),
('Delta Air Lines', 303, 'JFK', '2025-07-08', '08:30:00', 'ORD', '2025-07-08', '10:30:00', 275.00, 'on-time', 3),
('Delta Air Lines', 304, 'ORD', '2025-07-20', '10:00:00', 'DFW', '2025-07-20', '12:30:00', 285.00, 'delayed', 1),
('Delta Air Lines', 305, 'JFK', '2025-08-05', '23:00:00', 'LHR', '2025-08-06', '11:00:00', 755.00, 'on-time', 2),
('Delta Air Lines', 306, 'LAX', '2025-08-15', '22:30:00', 'NRT', '2025-08-16', '04:00:00', 960.00, 'on-time', 3),
('Delta Air Lines', 307, 'JFK', '2025-09-05', '19:00:00', 'CDG', '2025-09-06', '08:30:00', 825.00, 'on-time', 1),
('Delta Air Lines', 308, 'DFW', '2025-09-25', '08:00:00', 'LAX', '2025-09-25', '10:00:00', 295.00, 'delayed', 2),
('Delta Air Lines', 309, 'JFK', '2025-10-20', '14:00:00', 'PVG', '2025-10-21', '18:00:00', 860.00, 'on-time', 3),
('Delta Air Lines', 310, 'LAX', '2025-11-10', '11:00:00', 'SYD', '2025-11-11', '19:00:00', 1210.00, 'on-time', 1),
('Delta Air Lines', 311, 'ORD', '2025-12-05', '07:00:00', 'JFK', '2025-12-05', '10:00:00', 300.00, 'on-time', 2),
('Delta Air Lines', 312, 'JFK', '2025-12-18', '17:00:00', 'DXB', '2025-12-19', '14:00:00', 1110.00, 'delayed', 3),
('Delta Air Lines', 313, 'LAX', '2025-12-30', '09:00:00', 'ORD', '2025-12-30', '15:00:00', 325.00, 'on-time', 1),
-- United Airlines flights
('United Airlines', 401, 'JFK', '2025-06-12', '06:00:00', 'LAX', '2025-06-12', '09:00:00', 340.00, 'on-time', 1),
('United Airlines', 402, 'LAX', '2025-06-25', '17:00:00', 'JFK', '2025-06-26', '01:00:00', 370.00, 'on-time', 2),
('United Airlines', 403, 'JFK', '2025-07-12', '11:00:00', 'ORD', '2025-07-12', '13:00:00', 270.00, 'delayed', 3),
('United Airlines', 404, 'ORD', '2025-07-25', '08:00:00', 'DFW', '2025-07-25', '10:30:00', 280.00, 'on-time', 1),
('United Airlines', 405, 'JFK', '2025-08-10', '20:00:00', 'LHR', '2025-08-11', '08:00:00', 745.00, 'on-time', 2),
('United Airlines', 406, 'LAX', '2025-08-25', '21:30:00', 'NRT', '2025-08-26', '03:30:00', 940.00, 'on-time', 3),
('United Airlines', 407, 'JFK', '2025-09-15', '18:00:00', 'CDG', '2025-09-16', '07:30:00', 815.00, 'delayed', 1),
('United Airlines', 408, 'DFW', '2025-09-30', '09:00:00', 'LAX', '2025-09-30', '11:00:00', 290.00, 'on-time', 2),
('United Airlines', 409, 'JFK', '2025-10-25', '13:00:00', 'PVG', '2025-10-26', '17:00:00', 840.00, 'on-time', 3),
('United Airlines', 410, 'LAX', '2025-11-15', '12:00:00', 'SYD', '2025-11-16', '20:00:00', 1190.00, 'on-time', 1),
('United Airlines', 411, 'ORD', '2025-12-08', '06:30:00', 'JFK', '2025-12-08', '09:30:00', 285.00, 'delayed', 2),
('United Airlines', 412, 'JFK', '2025-12-22', '15:30:00', 'DXB', '2025-12-23', '13:30:00', 1090.00, 'on-time', 3),
('United Airlines', 413, 'LAX', '2025-12-31', '10:00:00', 'JFK', '2025-12-31', '18:00:00', 395.00, 'on-time', 1);

-- Insert Tickets (purchases from June 1 to December 31, 2025)
INSERT INTO Ticket (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   card_type, card_number, card_name, card_expiry, purchase_date, purchase_time) VALUES
-- June 2025 tickets
('john.doe@email.com', 'Jet Blue', 101, '2025-06-05', '08:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-06-01', '14:30:00'),
('jane.smith@email.com', 'Delta Air Lines', 301, '2025-06-03', '09:00:00', 
 'debit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-06-02', '10:15:00'),
('bob.zhang@email.com', 'American Airlines', 201, '2025-06-08', '07:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-06-05', '16:45:00'),
('alice.johnson@email.com', 'Jet Blue', 103, '2025-06-15', '10:30:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-06-10', '09:20:00'),
('charlie.brown@email.com', 'United Airlines', 401, '2025-06-12', '06:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-06-08', '11:00:00'),
('john.doe@email.com', 'Delta Air Lines', 302, '2025-06-18', '16:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-06-15', '15:30:00'),
('jane.smith@email.com', 'Jet Blue', 102, '2025-06-10', '14:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-06-08', '10:45:00'),
-- July 2025 tickets
('bob.zhang@email.com', 'Jet Blue', 105, '2025-07-01', '22:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-06-25', '14:20:00'),
('alice.johnson@email.com', 'American Airlines', 203, '2025-07-05', '09:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-07-01', '08:30:00'),
('charlie.brown@email.com', 'Delta Air Lines', 303, '2025-07-08', '08:30:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-07-05', '12:15:00'),
('john.doe@email.com', 'Jet Blue', 106, '2025-07-05', '12:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-07-02', '16:00:00'),
('jane.smith@email.com', 'American Airlines', 204, '2025-07-15', '21:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-07-10', '11:30:00'),
('bob.zhang@email.com', 'Delta Air Lines', 304, '2025-07-20', '10:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-07-18', '09:45:00'),
-- August 2025 tickets
('alice.johnson@email.com', 'Jet Blue', 108, '2025-08-15', '08:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-08-01', '10:20:00'),
('charlie.brown@email.com', 'American Airlines', 205, '2025-08-01', '08:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-07-28', '14:00:00'),
('john.doe@email.com', 'Delta Air Lines', 305, '2025-08-05', '23:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-08-01', '15:30:00'),
('jane.smith@email.com', 'United Airlines', 405, '2025-08-10', '20:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-08-05', '11:15:00'),
('bob.zhang@email.com', 'Jet Blue', 109, '2025-08-20', '14:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-08-15', '13:20:00'),
('alice.johnson@email.com', 'American Airlines', 206, '2025-08-20', '10:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-08-18', '09:00:00'),
-- September 2025 tickets
('charlie.brown@email.com', 'Jet Blue', 110, '2025-09-10', '20:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-09-01', '10:30:00'),
('john.doe@email.com', 'Delta Air Lines', 307, '2025-09-05', '19:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-09-02', '14:45:00'),
('jane.smith@email.com', 'United Airlines', 407, '2025-09-15', '18:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-09-10', '12:00:00'),
('bob.zhang@email.com', 'Delta Air Lines', 308, '2025-09-25', '08:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-09-20', '16:20:00'),
('alice.johnson@email.com', 'United Airlines', 408, '2025-09-30', '09:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-09-25', '08:15:00'),
-- October 2025 tickets
('charlie.brown@email.com', 'Jet Blue', 111, '2025-10-05', '10:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-10-01', '11:00:00'),
('john.doe@email.com', 'American Airlines', 208, '2025-10-15', '22:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-10-10', '15:30:00'),
('jane.smith@email.com', 'Delta Air Lines', 309, '2025-10-20', '14:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-10-15', '10:45:00'),
('bob.zhang@email.com', 'United Airlines', 409, '2025-10-25', '13:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-10-20', '14:20:00'),
-- November 2025 tickets
('alice.johnson@email.com', 'Jet Blue', 112, '2025-11-15', '15:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-11-01', '09:30:00'),
('charlie.brown@email.com', 'American Airlines', 209, '2025-11-05', '06:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-11-02', '12:15:00'),
('john.doe@email.com', 'Delta Air Lines', 310, '2025-11-10', '11:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-11-05', '16:00:00'),
('jane.smith@email.com', 'United Airlines', 410, '2025-11-15', '12:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-11-10', '10:20:00'),
-- December 2025 tickets
('bob.zhang@email.com', 'Jet Blue', 113, '2025-12-10', '11:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-12-01', '14:45:00'),
('alice.johnson@email.com', 'Delta Air Lines', 311, '2025-12-05', '07:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-12-02', '08:30:00'),
('charlie.brown@email.com', 'United Airlines', 411, '2025-12-08', '06:30:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-12-05', '11:15:00'),
('john.doe@email.com', 'American Airlines', 210, '2025-12-15', '11:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-12-10', '15:00:00'),
('jane.smith@email.com', 'Jet Blue', 114, '2025-12-20', '07:30:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-12-15', '10:30:00'),
('bob.zhang@email.com', 'Delta Air Lines', 312, '2025-12-18', '17:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-12-16', '13:20:00'),
('alice.johnson@email.com', 'United Airlines', 412, '2025-12-22', '15:30:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-12-18', '09:45:00'),
('charlie.brown@email.com', 'Jet Blue', 115, '2025-12-25', '08:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-12-20', '12:00:00'),
('john.doe@email.com', 'American Airlines', 211, '2025-12-22', '13:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-12-21', '14:30:00'),
('jane.smith@email.com', 'American Airlines', 212, '2025-12-28', '16:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-12-25', '10:15:00'),
('bob.zhang@email.com', 'Delta Air Lines', 313, '2025-12-30', '09:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-12-28', '16:20:00'),
('alice.johnson@email.com', 'United Airlines', 413, '2025-12-31', '10:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-12-30', '08:00:00');

-- Insert Reviews (for past flights - flights that occurred before current date)
-- Note: These reviews are for flights that have already occurred
INSERT INTO Review (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   rating, comment) VALUES
('john.doe@email.com', 'Jet Blue', 101, '2025-06-05', '08:00:00', 
 5, 'Excellent flight! Very smooth and comfortable. Great service from the crew.'),
('jane.smith@email.com', 'Delta Air Lines', 301, '2025-06-03', '09:00:00', 
 4, 'Good flight overall. Seats were comfortable but food could be better.'),
('bob.zhang@email.com', 'American Airlines', 201, '2025-06-08', '07:00:00', 
 5, 'Outstanding service! Will definitely fly with them again.'),
('alice.johnson@email.com', 'Jet Blue', 103, '2025-06-15', '10:30:00', 
 3, 'Flight was okay. Some delays but staff handled it well.'),
('charlie.brown@email.com', 'United Airlines', 401, '2025-06-12', '06:00:00', 
 4, 'Pleasant experience. Clean aircraft and friendly staff.'),
('john.doe@email.com', 'Delta Air Lines', 302, '2025-06-18', '16:00:00', 
 5, 'Perfect flight! On time and very comfortable.'),
('jane.smith@email.com', 'Jet Blue', 102, '2025-06-10', '14:00:00', 
 4, 'Great value for money. Would recommend to others.');
