# Airline Reservation System - Part 3

This is a Flask web application for an airline reservation system that allows customers to search and purchase flight tickets, and airline staff to manage flights and view reports.

## Prerequisites

Before setting up the application, ensure you have the following installed:

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **MySQL Server** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)
- **pip** (usually comes with Python)

## Database Setup

### 1. Install and Start MySQL

Install MySQL using Homebrew:

```bash
brew install mysql
brew services start mysql
```

### 2. Set Up the Database

**Step 1:** Navigate to the project directory:

```bash
cd "/path/to/project/pt3"
```

**Step 2:** Create the database:

```bash
mysql -e "CREATE DATABASE airline_reservation;"
```

**Step 3:** Set up the database schema (creates all tables):

```bash
mysql airline_reservation < schema.sql
```

**Step 4:** Load sample data (optional but recommended for testing):

```bash
mysql airline_reservation < sample_data.sql
```

**Note:** The sample data includes:
- 4 airlines (Jet Blue, American Airlines, Delta Air Lines, United Airlines)
- 10 airports
- 12 airplanes (3 per airline)
- 5 customers (with passwords: `password123`, `securepass`, `mypassword`, `alice123`, `charlie456`)
- 8 staff members (2 per airline, with passwords: `staffpass123`, `staffpass456`)
- 52 flights spanning June 1 to December 31, 2025
- 35+ tickets with purchase dates from June 1 to December 31, 2025
- Sample reviews for past flights

## Application Setup

### 1. Navigate to Project Directory

Navigate to the `pt3` directory in Terminal:

```bash
cd "/Users/willem/Library/CloudStorage/GoogleDrive-wdn2012@nyu.edu/My Drive/F2025/Intro to Databases/project/pt3"
```

**Tip:** You can drag and drop the `pt3` folder from Finder into Terminal to automatically paste the path.

### 2. Create Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies:

```bash
python3 -m venv project
```

Activate the virtual environment:

```bash
source project/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- mysql-connector-python 8.2.0
- Werkzeug 3.0.1

### 4. Configure Database Connection

The application uses environment variables for database configuration. You can either:

**Option A: Set Environment Variables**

```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DATABASE=airline_reservation
export SECRET_KEY=your-secret-key-here
```

**Note:** Replace `your_password` with your MySQL root password (or leave it empty if you haven't set a password).

**Option B: Use Default Values**

If you don't set environment variables, the application will use these defaults (defined in `config.py`):
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: `` (empty)
- Database: `airline_reservation`
- Secret Key: `dev-secret-key-change-in-production`

**Note:** Make sure your MySQL root password matches what you set (or leave it empty if you haven't set a password).

## Running the Application

### 1. Start the Flask Application

```bash
python app.py
```

Or:

```bash
flask run
```

The application will start on `http://localhost:5000` by default.

### 2. Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

## Application Features

### Customer Features
- **Register/Login** - Create a customer account or login
- **Search Flights** - Search for available flights by source, destination, and date
- **Purchase Tickets** - Purchase tickets for available flights
- **View My Flights** - View purchased flights with filtering options
- **Write Reviews** - Review past flights with ratings and comments

### Staff Features
- **Register/Login** - Create a staff account or login
- **View Flights** - View all flights for your airline with filtering
- **Create Flights** - Create new flights
- **Change Flight Status** - Update flight status (on-time/delayed)
- **Add Airplanes** - Add new airplanes to your airline
- **View Customers** - View all customers on a specific flight
- **View Ratings** - View flight ratings and reviews
- **View Reports** - Generate ticket sales reports

## Troubleshooting

### Database Connection Issues

If you encounter database connection errors:

1. **Verify MySQL is running:**
   ```bash
   brew services list
   mysql -u root -p
   ```

2. **Check database credentials** in `config.py` or environment variables

3. **Verify database and tables exist:**
   ```bash
   mysql -u root -p
   ```
   
   Then in MySQL:
   ```sql
   SHOW DATABASES;
   USE airline_reservation;
   SHOW TABLES;
   EXIT;
   ```

### Port Already in Use

If port 5000 is already in use:

```bash
# Set a different port
export PORT=5001
python app.py
```

Or modify `app.py` to use a different port.

### Module Not Found Errors

Make sure you've activated your virtual environment and installed all dependencies:

```bash
source project/bin/activate
pip install -r requirements.txt
```

## Sample Login Credentials

If you loaded the sample data, you can use these credentials:

**Customer:**
- Email: `john.doe@email.com`
- Password: `password123`

**Staff (all use password `staffpass123` or `staffpass456`):**
- Jet Blue: `staff001` or `staff002`
- American Airlines: `aa_staff001` or `aa_staff002`
- Delta Air Lines: `delta_staff001` or `delta_staff002`
- United Airlines: `ua_staff001` or `ua_staff002`

## Project Structure

```
pt3/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── database.py         # Database connection utilities
├── schema.sql          # Database schema
├── sample_data.sql     # Sample data for testing
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
├── static/             # CSS and static files
└── README.md           # This file
```

## Notes

- The application uses MD5 hashing for passwords (as specified in requirements)
- Sessions are used to maintain user login state
- The application supports both customer and staff user types
- All database queries use prepared statements for security

