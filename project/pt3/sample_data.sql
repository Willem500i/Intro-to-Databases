-- Insert Airline
INSERT INTO Airline (name) VALUES ('Jet Blue');

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
('Jet Blue', 1, 200, 'Boeing', 5),
('Jet Blue', 2, 180, 'Airbus', 3),
('Jet Blue', 3, 220, 'Boeing', 7);

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
('staff001', MD5('staffpass123'), 'Sarah', 'Johnson', '1988-03-20', 'Jet Blue', 'sarah.johnson@jetblue.com'),
('staff002', MD5('staffpass456'), 'Michael', 'Chen', '1990-06-15', 'Jet Blue', 'michael.chen@jetblue.com'),
('staff003', MD5('staffpass789'), 'Emily', 'Rodriguez', '1985-09-30', 'Jet Blue', 'emily.rodriguez@jetblue.com');

-- Insert Phone numbers for staff
INSERT INTO Phone (staff_username, phone_number) VALUES
('staff001', '718-555-1000'),
('staff001', '718-555-1001'),
('staff002', '212-555-2000'),
('staff003', '310-555-3000'),
('staff003', '310-555-3001');

-- Insert 25 Flights
INSERT INTO Flight (airline_name, flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, status, airplane_id) VALUES
-- Original flights
('Jet Blue', 101, 'JFK', '2025-12-15', '08:00:00', 'PVG', '2025-12-16', '12:00:00', 850.00, 'on-time', 1),
('Jet Blue', 102, 'PVG', '2025-12-20', '14:00:00', 'JFK', '2025-12-20', '18:00:00', 900.00, 'on-time', 2),
('Jet Blue', 103, 'JFK', '2025-12-18', '10:30:00', 'LAX', '2025-12-18', '13:30:00', 350.00, 'on-time', 3),
('Jet Blue', 104, 'LAX', '2025-12-22', '09:00:00', 'JFK', '2025-12-22', '17:00:00', 380.00, 'delayed', 1),
('Jet Blue', 105, 'JFK', '2025-12-25', '15:00:00', 'PVG', '2025-12-26', '19:00:00', 920.00, 'delayed', 2),
-- New flights - Domestic USA routes
('Jet Blue', 106, 'JFK', '2025-12-16', '06:00:00', 'ORD', '2025-12-16', '08:30:00', 280.00, 'on-time', 1),
('Jet Blue', 107, 'ORD', '2025-12-17', '09:00:00', 'LAX', '2025-12-17', '11:30:00', 320.00, 'on-time', 2),
('Jet Blue', 108, 'LAX', '2025-12-19', '14:00:00', 'DFW', '2025-12-19', '19:00:00', 290.00, 'on-time', 3),
('Jet Blue', 109, 'DFW', '2025-12-21', '07:30:00', 'JFK', '2025-12-21', '12:00:00', 310.00, 'on-time', 1),
('Jet Blue', 110, 'ORD', '2025-12-23', '11:00:00', 'DFW', '2025-12-23', '13:30:00', 250.00, 'delayed', 2),
-- New flights - International routes
('Jet Blue', 111, 'JFK', '2025-12-17', '22:00:00', 'LHR', '2025-12-18', '10:00:00', 750.00, 'on-time', 1),
('Jet Blue', 112, 'LHR', '2025-12-19', '12:00:00', 'JFK', '2025-12-19', '15:30:00', 780.00, 'on-time', 2),
('Jet Blue', 113, 'LAX', '2025-12-20', '23:30:00', 'NRT', '2025-12-21', '05:00:00', 950.00, 'on-time', 3),
('Jet Blue', 114, 'NRT', '2025-12-22', '14:00:00', 'LAX', '2025-12-22', '08:00:00', 980.00, 'delayed', 1),
('Jet Blue', 115, 'JFK', '2025-12-24', '20:00:00', 'CDG', '2025-12-25', '09:30:00', 820.00, 'on-time', 2),
('Jet Blue', 116, 'CDG', '2025-12-26', '11:00:00', 'JFK', '2025-12-26', '14:00:00', 840.00, 'on-time', 3),
('Jet Blue', 117, 'LAX', '2025-12-27', '10:00:00', 'SYD', '2025-12-28', '18:00:00', 1200.00, 'on-time', 1),
('Jet Blue', 118, 'SYD', '2025-12-29', '22:00:00', 'LAX', '2025-12-30', '06:00:00', 1250.00, 'on-time', 2),
('Jet Blue', 119, 'JFK', '2025-12-28', '15:00:00', 'DXB', '2025-12-29', '12:00:00', 1100.00, 'delayed', 3),
('Jet Blue', 120, 'DXB', '2025-12-30', '02:00:00', 'JFK', '2025-12-30', '10:30:00', 1120.00, 'on-time', 1),
-- More domestic routes
('Jet Blue', 121, 'ORD', '2025-12-24', '08:00:00', 'LAX', '2025-12-24', '10:30:00', 330.00, 'on-time', 2),
('Jet Blue', 122, 'DFW', '2025-12-26', '13:00:00', 'ORD', '2025-12-26', '15:30:00', 270.00, 'on-time', 3),
('Jet Blue', 123, 'LAX', '2025-12-28', '16:00:00', 'ORD', '2025-12-28', '22:30:00', 340.00, 'delayed', 1),
('Jet Blue', 124, 'JFK', '2025-12-29', '06:30:00', 'DFW', '2025-12-29', '10:00:00', 300.00, 'on-time', 2),
('Jet Blue', 125, 'ORD', '2025-12-31', '18:00:00', 'JFK', '2025-12-31', '21:00:00', 290.00, 'on-time', 3);

-- Insert Tickets (purchases)
INSERT INTO Ticket (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   card_type, card_number, card_name, card_expiry, purchase_date, purchase_time) VALUES
('john.doe@email.com', 'Jet Blue', 101, '2025-12-15', '08:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-11-01', '14:30:00'),
('jane.smith@email.com', 'Jet Blue', 103, '2025-12-18', '10:30:00', 
 'debit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-11-05', '10:15:00'),
('bob.zhang@email.com', 'Jet Blue', 104, '2025-12-22', '09:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-11-10', '16:45:00'),
('alice.johnson@email.com', 'Jet Blue', 106, '2025-12-16', '06:00:00', 
 'credit', '4111111111112222', 'Alice Johnson', '2027-06-30', '2025-11-02', '09:20:00'),
('charlie.brown@email.com', 'Jet Blue', 111, '2025-12-17', '22:00:00', 
 'debit', '5555555555555555', 'Charlie Brown', '2026-12-31', '2025-11-08', '11:00:00'),
('john.doe@email.com', 'Jet Blue', 112, '2025-12-19', '12:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-11-12', '15:30:00'),
('jane.smith@email.com', 'Jet Blue', 115, '2025-12-24', '20:00:00', 
 'credit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-11-15', '10:45:00');

-- Insert Reviews (for past flights - need to add a past flight first)
-- First, add a past flight that customers can review
INSERT INTO Flight (airline_name, flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, status, airplane_id) VALUES
('Jet Blue', 100, 'JFK', '2025-10-01', '08:00:00', 'LAX', '2025-10-01', '11:00:00', 300.00, 'on-time', 1);

-- Add a ticket for the past flight
INSERT INTO Ticket (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   card_type, card_number, card_name, card_expiry, purchase_date, purchase_time) VALUES
('john.doe@email.com', 'Jet Blue', 100, '2025-10-01', '08:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-09-15', '12:00:00');

-- Insert Reviews (for past flights)
INSERT INTO Review (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   rating, comment) VALUES
('john.doe@email.com', 'Jet Blue', 100, '2025-10-01', '08:00:00', 
 5, 'Excellent flight! Very smooth and comfortable. Great service from the crew.');
