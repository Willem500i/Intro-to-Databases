-- Insert Airline
INSERT INTO Airline (name) VALUES ('Jet Blue');

-- Insert Airports
INSERT INTO Airport (airport_code, city, country, airport_type) VALUES
('JFK', 'New York City', 'USA', 'international'),
('PVG', 'Shanghai', 'China', 'international'),
('LAX', 'Los Angeles', 'USA', 'international');

-- Insert Customers
INSERT INTO Customer (customer_email, name, password, building_number, street, city, state, 
                     phone_number, passport_number, passport_expiration, passport_country, date_of_birth) VALUES
('john.doe@email.com', 'John Doe', MD5('password123'), 123, 'Main Street', 'New York', 'NY', 
 '212-555-0101', 'P123456', '2027-12-31', 'USA', '1990-05-15'),
('jane.smith@email.com', 'Jane Smith', MD5('securepass'), 456, 'Park Avenue', 'Los Angeles', 'CA', 
 '310-555-0202', 'P789012', '2026-06-30', 'USA', '1985-08-22'),
('bob.zhang@email.com', 'Bob Zhang', MD5('mypassword'), 789, 'Broadway', 'New York', 'NY', 
 '212-555-0303', 'P345678', '2028-03-15', 'USA', '1992-11-10');

-- Insert Airplanes
INSERT INTO Airplane (airline_name, id_number, num_seats, manufacturer, age) VALUES
('Jet Blue', 1, 200, 'Boeing', 5),
('Jet Blue', 2, 180, 'Airbus', 3),
('Jet Blue', 3, 220, 'Boeing', 7);

-- Insert Airline Staff
INSERT INTO AirlineStaff (username, password, name_first, name_last, date_of_birth, airline_name, email) VALUES
('staff001', MD5('staffpass123'), 'Sarah', 'Johnson', '1988-03-20', 'Jet Blue', 'sarah.johnson@jetblue.com');

-- Insert Phone numbers for staff
INSERT INTO Phone (staff_username, phone_number) VALUES
('staff001', '718-555-1000'),
('staff001', '718-555-1001');

-- Insert Future Flights (some on-time, some delayed)
INSERT INTO Flight (airline_name, flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, status, airplane_airline, airplane_id) VALUES
-- Future on-time flights
('Jet Blue', 101, 'JFK', '2025-12-15', '08:00:00', 'PVG', '2025-12-16', '12:00:00', 850.00, 'on-time', 'Jet Blue', 1),
('Jet Blue', 102, 'PVG', '2025-12-20', '14:00:00', 'JFK', '2025-12-20', '18:00:00', 900.00, 'on-time', 'Jet Blue', 2),
('Jet Blue', 103, 'JFK', '2025-12-18', '10:30:00', 'LAX', '2025-12-18', '13:30:00', 350.00, 'on-time', 'Jet Blue', 3),
-- Future delayed flights
('Jet Blue', 104, 'LAX', '2025-12-22', '09:00:00', 'JFK', '2025-12-22', '17:00:00', 380.00, 'delayed', 'Jet Blue', 1),
('Jet Blue', 105, 'JFK', '2025-12-25', '15:00:00', 'PVG', '2025-12-26', '19:00:00', 920.00, 'delayed', 'Jet Blue', 2),
-- Past flight for reviews
('Jet Blue', 100, 'JFK', '2025-10-01', '08:00:00', 'LAX', '2025-10-01', '11:00:00', 300.00, 'on-time', 'Jet Blue', 1);

-- Insert Tickets (purchases)
INSERT INTO Ticket (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   card_type, card_number, card_name, card_expiry, purchase_date, purchase_time) VALUES
('john.doe@email.com', 'Jet Blue', 101, '2025-12-15', '08:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-11-01', '14:30:00'),
('jane.smith@email.com', 'Jet Blue', 103, '2025-12-18', '10:30:00', 
 'debit', '5555555555554444', 'Jane Smith', '2026-08-31', '2025-11-05', '10:15:00'),
('bob.zhang@email.com', 'Jet Blue', 104, '2025-12-22', '09:00:00', 
 'credit', '378282246310005', 'Bob Zhang', '2028-03-31', '2025-11-10', '16:45:00'),
('john.doe@email.com', 'Jet Blue', 100, '2025-10-01', '08:00:00', 
 'credit', '4111111111111111', 'John Doe', '2027-12-31', '2025-09-15', '12:00:00');

-- Insert Reviews (for past flights)
INSERT INTO Review (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time,
                   rating, comment, review_date) VALUES
('john.doe@email.com', 'Jet Blue', 100, '2025-10-01', '08:00:00', 
 5, 'Excellent flight! Very smooth and comfortable.', '2025-10-02 10:30:00');