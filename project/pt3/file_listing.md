# File Listing and Purpose

## Python Files

### app.py
Main Flask application file containing all route handlers and business logic. This file:
- Defines all URL routes for customer and staff functionality
- Handles user authentication (login/logout/registration)
- Implements customer features: flight search, ticket purchase, viewing flights, writing reviews
- Implements staff features: flight management, airplane management, customer viewing, ratings viewing, reports generation
- Uses prepared statements for all database queries to prevent SQL injection
- Manages user sessions and access control

### config.py
Configuration file that manages database connection settings and application secrets:
- Reads database credentials from environment variables (for production) or uses defaults (for local development)
- Configures MySQL connection parameters (host, port, user, password, database name)
- Sets Flask secret key for session management
- Allows easy switching between local and production environments

### database.py
Database utility module that provides connection management and query execution:
- `get_db_connection()`: Establishes connection to MySQL database using settings from config.py
- `execute_query()`: Executes SQL queries with optional parameters and returns results
- `execute_prepared_query()`: Executes parameterized queries (prepared statements) for security
- Handles connection errors gracefully and manages connection lifecycle (open/close)
- Uses dictionary cursors to return results as dictionaries for easier access

## SQL Files

### schema.sql
Database schema definition file that creates all tables and relationships:
- Defines table structures: Airport, Airline, Airplane, Flight, Customer, AirlineStaff, Phone, Ticket, Review
- Sets up primary keys, foreign keys, and referential integrity constraints
- Includes CHECK constraints for data validation (e.g., status values, rating range, card types)
- Uses AUTO_INCREMENT for ticket_id generation
- Establishes relationships between entities (e.g., Flight references Airline, Ticket references Flight and Customer)

### sample_data.sql
Sample data file for testing and demonstration:
- Inserts 4 airlines (Jet Blue, American Airlines, Delta Air Lines, United Airlines)
- Inserts 10 airports across different countries
- Inserts 12 airplanes (3 per airline)
- Inserts 5 sample customers with hashed passwords
- Inserts 8 staff members (2 per airline)
- Inserts 52 flights spanning June 1 to December 31, 2025
- Inserts 35+ tickets with purchase dates throughout the date range
- Inserts sample reviews for past flights
- Provides test credentials for login testing

## HTML Template Files

### base.html
Base template that provides the common structure for all pages:
- Defines HTML structure with navigation bar
- Includes Bootstrap CSS for styling
- Displays flash messages (success/error notifications)
- Provides navigation links based on user login status (customer/staff/logged out)
- Contains logout functionality
- Serves as parent template that other templates extend

### index.html
Home page template:
- Landing page accessible to all users (logged in or not)
- Displays welcome message and basic information about the airline reservation system
- Provides links to registration and login
- Shows different content based on user login status

### login.html
User login page template:
- Unified login form for both customers and staff
- Single form that handles both customer (email) and staff (username) authentication
- Displays error messages for invalid credentials
- Redirects users to appropriate home page after successful login

### register.html
User registration page template:
- Unified registration form for both customers and staff
- Toggle between customer and staff registration modes
- Customer registration: email, name, password fields
- Staff registration: username, password, name, date of birth, airline selection, email
- Validates password confirmation
- Shows list of available airlines for staff registration

### customer_home.html
Customer home page template:
- Displays customer's future flights by default
- Shows flight details: airline, flight number, departure/arrival airports and cities, dates, times, status, ticket ID
- Displays purchase date and time for each ticket
- Provides link to view all flights with filtering options
- Navigation to search flights, view reviews, and logout

### view_my_flights.html
Customer flight viewing page with filtering:
- Displays all customer's flights (past, future, or all)
- Filtering options: date range, source airport/city, destination airport/city, flight type (future/past/all)
- Shows same flight details as customer home
- Allows customers to see their complete flight history

### search_flights.html
Public flight search page:
- Available to all users (no login required)
- Search form with: source, destination, departure date, return date (optional), trip type
- Allows searching by airport code or city name
- Displays search results on separate page

### search_results.html
Flight search results page:
- Displays matching flights from search
- Shows flight details: airline, flight number, departure/arrival airports and cities, dates, times, price, status
- Provides purchase button for each flight (requires customer login)
- Shows error messages if no flights found or database errors occur

### purchase_ticket.html
Ticket purchase page:
- Displays flight details for the selected flight
- Shows available seats remaining
- Payment form: card type, card number, cardholder name, card expiry month/year
- Validates payment information before processing
- Only accessible to logged-in customers
- Prevents purchase of past flights or sold-out flights

### customer_reviews.html
Customer review page:
- Lists all past flights that customer can review
- Shows flight details and existing review (if any)
- Allows customers to submit new reviews or update existing reviews
- Review form: rating (1-5 stars) and optional comment
- Only shows flights that have already occurred

### staff_home.html
Staff home page:
- Displays flights for staff's airline (next 30 days by default)
- Shows flight details: airline, flight number, departure/arrival airports and cities, dates, times, price, status
- Displays number of tickets sold for each flight
- Navigation to all staff functions

### staff_view_flights.html
Staff flight viewing page with filtering:
- Displays all flights for staff's airline
- Filtering options: date range, source airport/city, destination airport/city, flight type (future/past/all)
- Shows tickets sold count for each flight
- Provides links to view customers for each flight

### staff_create_flight.html
Staff flight creation page:
- Form to create new flights
- Fields: flight number, departure airport, departure date/time, arrival airport, arrival date/time, base price, airplane selection
- Dropdown lists for airports and airplanes (filtered by staff's airline)
- Validates that airplane belongs to staff's airline
- Prevents duplicate flights (same airline, number, date, time)

### staff_change_status.html
Staff flight status update page:
- Lists all flights for staff's airline
- Allows changing flight status between "on-time" and "delayed"
- Dropdown selection for each flight to update status
- Verifies staff can only change status for their airline's flights

### staff_add_airplane.html
Staff airplane management page:
- Displays all airplanes for staff's airline
- Form to add new airplanes
- Fields: airplane ID, number of seats, manufacturer, age
- Validates that airplane ID is unique for the airline
- Shows list of existing airplanes for reference

### staff_view_customers.html
Staff customer viewing page:
- Displays all customers who purchased tickets for a specific flight
- Shows customer details: ticket ID, email, name, phone number, passport number
- Displays purchase date and time
- Shows flight details at the top
- Only accessible for flights belonging to staff's airline

### staff_view_ratings.html
Staff ratings overview page:
- Lists all flights for staff's airline with average ratings
- Shows flight details and number of reviews
- Displays average rating for each flight
- Provides links to view detailed reviews for each flight

### staff_view_flight_reviews.html
Staff detailed reviews page:
- Shows all individual reviews for a specific flight
- Displays customer name, rating, and comment for each review
- Shows average rating for the flight
- Only accessible for flights belonging to staff's airline

### staff_view_reports.html
Staff sales reports page:
- Generates ticket sales reports for staff's airline
- Report types: date range, last month, last year
- Shows tickets sold and total revenue per day or month
- Displays totals (total tickets sold, total revenue) for the report period
- Helps staff analyze sales performance

### staff_login.html, staff_register.html
Legacy staff-specific pages that redirect to unified login/register:
- These templates exist for backward compatibility
- All staff authentication now uses the unified login/register pages

## Static Files

### static/style.css
CSS stylesheet for application styling:
- Custom styles for the application
- Complements Bootstrap CSS framework
- Defines colors, spacing, and layout for consistent UI
- Styles for forms, tables, buttons, and navigation elements

## Configuration Files

### requirements.txt
Python package dependencies file:
- Lists all required Python packages and versions
- Flask==3.0.0: Web framework
- mysql-connector-python==8.2.0: MySQL database connector
- Werkzeug==3.0.1: WSGI utility library (dependency of Flask)
- Used by pip to install all dependencies: `pip install -r requirements.txt`

### README.md
Project documentation and setup instructions:
- Provides installation instructions for MySQL and Python
- Step-by-step database setup guide
- Application setup instructions (virtual environment, dependencies)
- Configuration instructions for database connection
- Running instructions
- Feature overview
- Sample login credentials
- Troubleshooting guide

