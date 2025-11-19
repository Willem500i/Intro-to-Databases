-- Create Airport table
CREATE TABLE Airport (
    airport_code VARCHAR(10) PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    airport_type VARCHAR(20) NOT NULL,
    CHECK (airport_type IN ('domestic', 'international', 'both'))
);

-- Create Airline table
CREATE TABLE Airline (
    name VARCHAR(100) PRIMARY KEY
);

-- Create Airplane table (Weak entity - depends on Airline)
CREATE TABLE Airplane (
    airline_name VARCHAR(100) NOT NULL,
    id_number INT NOT NULL,
    num_seats INT NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (airline_name, id_number),
    FOREIGN KEY (airline_name) REFERENCES Airline(name) ON DELETE CASCADE
);

-- Create Flight table (Weak entity - depends on Airline)
CREATE TABLE Flight (
    airline_name VARCHAR(100) NOT NULL,
    flight_number INT NOT NULL,
    departure_airport VARCHAR(10) NOT NULL,
    departure_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    arrival_airport VARCHAR(10) NOT NULL,
    arrival_date DATE NOT NULL,
    arrival_time TIME NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'on-time',
    airplane_id INT,
    PRIMARY KEY (airline_name, flight_number, departure_date, departure_time),
    FOREIGN KEY (airline_name) REFERENCES Airline(name) ON DELETE CASCADE,
    FOREIGN KEY (departure_airport) REFERENCES Airport(airport_code),
    FOREIGN KEY (arrival_airport) REFERENCES Airport(airport_code),
    FOREIGN KEY (airline_name, airplane_id) REFERENCES Airplane(airline_name, id_number),
    CHECK (status IN ('on-time', 'delayed'))
);

-- Create Customer table
CREATE TABLE Customer (
    customer_email VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    building_number INT,
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50),
    phone_number VARCHAR(20),
    passport_number VARCHAR(50),
    passport_expiration DATE,
    passport_country VARCHAR(100),
    date_of_birth DATE
);

-- Create AirlineStaff table
CREATE TABLE AirlineStaff (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    name_first VARCHAR(50) NOT NULL,
    name_last VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    airline_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    FOREIGN KEY (airline_name) REFERENCES Airline(name) ON DELETE CASCADE
);

-- Create Phone table (Weak entity - depends on AirlineStaff)
CREATE TABLE Phone (
    staff_username VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    PRIMARY KEY (staff_username, phone_number),
    FOREIGN KEY (staff_username) REFERENCES AirlineStaff(username) ON DELETE CASCADE
);

-- Create Ticket table
CREATE TABLE Ticket (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_email VARCHAR(100) NOT NULL,
    flight_airline VARCHAR(100) NOT NULL,
    flight_number INT NOT NULL,
    flight_departure_date DATE NOT NULL,
    flight_departure_time TIME NOT NULL,
    card_type VARCHAR(10) NOT NULL,
    card_number VARCHAR(20) NOT NULL,
    card_name VARCHAR(100) NOT NULL,
    card_expiry DATE NOT NULL,
    purchase_date DATE NOT NULL,
    purchase_time TIME NOT NULL,
    FOREIGN KEY (customer_email) REFERENCES Customer(customer_email) ON DELETE CASCADE,
    FOREIGN KEY (flight_airline, flight_number, flight_departure_date, flight_departure_time) 
        REFERENCES Flight(airline_name, flight_number, departure_date, departure_time),
    CHECK (card_type IN ('credit', 'debit'))
);

-- Create Review table
CREATE TABLE Review (
    customer_email VARCHAR(100) NOT NULL,
    flight_airline VARCHAR(100) NOT NULL,
    flight_number INT NOT NULL,
    flight_departure_date DATE NOT NULL,
    flight_departure_time TIME NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    PRIMARY KEY (customer_email, flight_airline, flight_number, flight_departure_date, flight_departure_time),
    FOREIGN KEY (customer_email) REFERENCES Customer(customer_email) ON DELETE CASCADE,
    FOREIGN KEY (flight_airline, flight_number, flight_departure_date, flight_departure_time) 
        REFERENCES Flight(airline_name, flight_number, departure_date, departure_time),
    CHECK (rating >= 1 AND rating <= 5)
);

