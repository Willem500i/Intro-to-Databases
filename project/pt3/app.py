from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
from datetime import datetime, date, time
from database import execute_prepared_query
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def require_customer_login(f):
    """Decorator to require customer login"""
    def decorated_function(*args, **kwargs):
        if 'user_type' not in session or session['user_type'] != 'customer':
            flash('Please login as a customer to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def require_staff_login(f):
    """Decorator to require staff login"""
    def decorated_function(*args, **kwargs):
        if 'user_type' not in session or session['user_type'] != 'staff':
            flash('Please login as airline staff to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def index():
    """Home page - shows different content based on login status"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Unified registration for customers and staff"""
    if request.method == 'POST':
        user_type = request.form.get('user_type')  # 'customer' or 'staff'
        
        if user_type == 'customer':
            # Customer registration
            email = request.form.get('email')
            name = request.form.get('name')
            password = request.form.get('password')
            password_confirm = request.form.get('password_confirm')
            
            # Validate inputs
            if not all([email, name, password]):
                flash('Please fill in all required fields.', 'error')
                return render_template('register.html')
            
            if password != password_confirm:
                flash('Passwords do not match.', 'error')
                return render_template('register.html')
            
            # Check if email already exists
            check_query = "SELECT customer_email FROM Customer WHERE customer_email = %s"
            existing = execute_prepared_query(check_query, (email,))
            
            if existing:
                flash('Email already registered. Please login instead.', 'error')
                return redirect(url_for('login'))
            
            # Hash password using MD5 as specified in requirements
            password_hash = hashlib.md5(password.encode()).hexdigest()
            
            # Insert new customer
            insert_query = """
                INSERT INTO Customer (customer_email, name, password)
                VALUES (%s, %s, %s)
            """
            
            result = execute_prepared_query(insert_query, (email, name, password_hash), fetch=False)
            
            if result is not None:
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Registration failed. Please try again.', 'error')
        
        elif user_type == 'staff':
            # Staff registration
            username = request.form.get('username')
            password = request.form.get('password')
            password_confirm = request.form.get('password_confirm')
            name_first = request.form.get('name_first')
            name_last = request.form.get('name_last')
            date_of_birth = request.form.get('date_of_birth')
            airline_name = request.form.get('airline_name')
            email = request.form.get('email')
            
            # Validate inputs
            if not all([username, password, name_first, name_last, airline_name, email]):
                flash('Please fill in all required fields.', 'error')
                airlines = execute_prepared_query("SELECT name FROM Airline")
                return render_template('register.html', airlines=airlines or [])
            
            if password != password_confirm:
                flash('Passwords do not match.', 'error')
                airlines = execute_prepared_query("SELECT name FROM Airline")
                return render_template('register.html', airlines=airlines or [])
            
            # Check if username already exists
            check_query = "SELECT username FROM AirlineStaff WHERE username = %s"
            existing = execute_prepared_query(check_query, (username,))
            
            if existing:
                flash('Username already registered. Please login instead.', 'error')
                return redirect(url_for('login'))
            
            # Verify airline exists
            airline_check = execute_prepared_query("SELECT name FROM Airline WHERE name = %s", (airline_name,))
            if not airline_check:
                flash('Invalid airline name.', 'error')
                airlines = execute_prepared_query("SELECT name FROM Airline")
                return render_template('register.html', airlines=airlines or [])
            
            # Hash password using MD5 as specified in requirements
            password_hash = hashlib.md5(password.encode()).hexdigest()
            
            # Insert new staff
            insert_query = """
                INSERT INTO AirlineStaff (username, password, name_first, name_last, 
                                        date_of_birth, airline_name, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            result = execute_prepared_query(insert_query, 
                (username, password_hash, name_first, name_last, 
                 date_of_birth if date_of_birth else None, airline_name, email), fetch=False)
            
            if result is not None:
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Registration failed. Please try again.', 'error')
        else:
            flash('Please select a user type.', 'error')
    
    # GET request - show registration form
    airlines = execute_prepared_query("SELECT name FROM Airline")
    return render_template('register.html', airlines=airlines or [])

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Unified login for customers and staff"""
    if request.method == 'POST':
        username = request.form.get('username')  # email for customers, username for staff
        password = request.form.get('password')
        
        # Hash password using MD5 as specified in requirements
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # Try customer login first (email as username)
        customer_query = "SELECT customer_email, name FROM Customer WHERE customer_email = %s AND password = %s"
        customer = execute_prepared_query(customer_query, (username, password_hash))
        
        if customer:
            session['user_type'] = 'customer'
            session['username'] = customer[0]['customer_email']
            session['name'] = customer[0]['name']
            flash('Login successful!', 'success')
            return redirect(url_for('customer_home'))
        
        # Try staff login
        staff_query = """
            SELECT username, name_first, name_last, airline_name 
            FROM AirlineStaff 
            WHERE username = %s AND password = %s
        """
        staff = execute_prepared_query(staff_query, (username, password_hash))
        
        if staff:
            session['user_type'] = 'staff'
            session['username'] = staff[0]['username']
            session['name'] = f"{staff[0]['name_first']} {staff[0]['name_last']}"
            session['airline_name'] = staff[0]['airline_name']
            flash('Login successful!', 'success')
            return redirect(url_for('staff_home'))
        
        # Neither customer nor staff found
        flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout and destroy session"""
    session.clear()
    flash('You have been logged out. Thank you for using our service!', 'info')
    return redirect(url_for('index'))

@app.route('/customer/home')
@require_customer_login
def customer_home():
    """Customer home page - View My Flights (default: future flights)"""
    # Get customer's future flights by default
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.arrival_date, f.arrival_time, f.base_price, f.status,
               t.ticket_id, t.purchase_date, t.purchase_time,
               a1.city as departure_city, a2.city as arrival_city
        FROM Ticket t
        JOIN Flight f ON t.flight_airline = f.airline_name 
            AND t.flight_number = f.flight_number
            AND t.flight_departure_date = f.departure_date
            AND t.flight_departure_time = f.departure_time
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE t.customer_email = %s
            AND CONCAT(f.departure_date, ' ', f.departure_time) > NOW()
        ORDER BY f.departure_date, f.departure_time
    """
    
    flights = execute_prepared_query(query, (session['username'],))
    
    return render_template('customer_home.html', flights=flights or [])

@app.route('/customer/flights', methods=['GET', 'POST'])
@require_customer_login
def view_my_flights():
    """View My Flights with filtering options"""
    if request.method == 'POST':
        start_date = request.form.get('start_date', '')
        end_date = request.form.get('end_date', '')
        source = request.form.get('source', '')
        destination = request.form.get('destination', '')
        flight_type = request.form.get('flight_type', 'future')  # future, past, all
        
        # Build query
        query = """
            SELECT f.airline_name, f.flight_number, f.departure_airport, 
                   f.departure_date, f.departure_time, f.arrival_airport,
                   f.arrival_date, f.arrival_time, f.base_price, f.status,
                   t.ticket_id, t.purchase_date, t.purchase_time,
                   a1.city as departure_city, a2.city as arrival_city
            FROM Ticket t
            JOIN Flight f ON t.flight_airline = f.airline_name 
                AND t.flight_number = f.flight_number
                AND t.flight_departure_date = f.departure_date
                AND t.flight_departure_time = f.departure_time
            JOIN Airport a1 ON f.departure_airport = a1.airport_code
            JOIN Airport a2 ON f.arrival_airport = a2.airport_code
            WHERE t.customer_email = %s
        """
        params = [session['username']]
        
        # Filter by date range
        if flight_type == 'future':
            query += " AND CONCAT(f.departure_date, ' ', f.departure_time) > NOW()"
        elif flight_type == 'past':
            query += " AND CONCAT(f.departure_date, ' ', f.departure_time) <= NOW()"
        # 'all' shows everything, no additional filter
        
        if start_date:
            query += " AND f.departure_date >= %s"
            params.append(start_date)
        
        if end_date:
            query += " AND f.departure_date <= %s"
            params.append(end_date)
        
        if source:
            query += " AND (f.departure_airport = %s OR a1.city LIKE %s)"
            params.extend([source, f'%{source}%'])
        
        if destination:
            query += " AND (f.arrival_airport = %s OR a2.city LIKE %s)"
            params.extend([destination, f'%{destination}%'])
        
        query += " ORDER BY f.departure_date, f.departure_time"
        
        flights = execute_prepared_query(query, params)
        
        return render_template('view_my_flights.html', flights=flights or [], 
                             start_date=start_date, end_date=end_date,
                             source=source, destination=destination, flight_type=flight_type)
    
    # Default: show future flights
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.arrival_date, f.arrival_time, f.base_price, f.status,
               t.ticket_id, t.purchase_date, t.purchase_time,
               a1.city as departure_city, a2.city as arrival_city
        FROM Ticket t
        JOIN Flight f ON t.flight_airline = f.airline_name 
            AND t.flight_number = f.flight_number
            AND t.flight_departure_date = f.departure_date
            AND t.flight_departure_time = f.departure_time
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE t.customer_email = %s
            AND CONCAT(f.departure_date, ' ', f.departure_time) > NOW()
        ORDER BY f.departure_date, f.departure_time
    """
    
    flights = execute_prepared_query(query, (session['username'],))
    return render_template('view_my_flights.html', flights=flights or [], 
                         start_date='', end_date='', source='', destination='', flight_type='future')

@app.route('/search_flights', methods=['GET', 'POST'])
def search_flights():
    """Public flight search - available to everyone"""
    if request.method == 'POST':
        source = request.form.get('source', '')
        destination = request.form.get('destination', '')
        departure_date = request.form.get('departure_date', '')
        return_date = request.form.get('return_date', '')
        trip_type = request.form.get('trip_type', 'one-way')
        
        # Build query based on search parameters
        query = """
            SELECT f.airline_name, f.flight_number, f.departure_airport, 
                   f.departure_date, f.departure_time, f.arrival_airport,
                   f.arrival_date, f.arrival_time, f.base_price, f.status,
                   a1.city as departure_city, a2.city as arrival_city
            FROM Flight f
            JOIN Airport a1 ON f.departure_airport = a1.airport_code
            JOIN Airport a2 ON f.arrival_airport = a2.airport_code
            WHERE CONCAT(f.departure_date, ' ', f.departure_time) > NOW()
        """
        params = []
        
        if source:
            query += " AND (f.departure_airport = %s OR a1.city LIKE %s)"
            params.extend([source, f'%{source}%'])
        
        if destination:
            query += " AND (f.arrival_airport = %s OR a2.city LIKE %s)"
            params.extend([destination, f'%{destination}%'])
        
        if departure_date:
            query += " AND f.departure_date = %s"
            params.append(departure_date)
        
        query += " ORDER BY f.departure_date, f.departure_time"
        
        try:
            flights = execute_prepared_query(query, params if params else None)
            return render_template('search_results.html', flights=flights or [], 
                                 source=source, destination=destination, 
                                 departure_date=departure_date, return_date=return_date)
        except Exception as e:
            return render_template('search_results.html', flights=[], 
                                 error=f"Database error: {str(e)}",
                                 source=source, destination=destination, 
                                 departure_date=departure_date, return_date=return_date)
    
    return render_template('search_flights.html')

@app.route('/purchase/<airline>/<int:flight_number>/<departure_date>/<departure_time>', methods=['GET', 'POST'])
@require_customer_login
def purchase_ticket(airline, flight_number, departure_date, departure_time):
    """Purchase ticket for a flight"""
    if request.method == 'POST':
        # Get flight details first to verify it exists and is in the future
        flight_query = """
            SELECT f.*, a.num_seats,
                   (SELECT COUNT(*) FROM Ticket t 
                    WHERE t.flight_airline = f.airline_name 
                    AND t.flight_number = f.flight_number
                    AND t.flight_departure_date = f.departure_date
                    AND t.flight_departure_time = f.departure_time) as tickets_sold
            FROM Flight f
            JOIN Airplane a ON f.airline_name = a.airline_name AND f.airplane_id = a.id_number
            WHERE f.airline_name = %s AND f.flight_number = %s 
            AND f.departure_date = %s AND f.departure_time = %s
        """
        flight = execute_prepared_query(flight_query, (airline, flight_number, departure_date, departure_time))
        
        if not flight:
            flash('Flight not found.', 'error')
            return redirect(url_for('search_flights'))
        
        flight = flight[0]
        
        # Check if flight is in the future
        # MySQL returns TIME as timedelta, convert to time object
        departure_time = flight['departure_time']
        if isinstance(departure_time, time):
            flight_time = departure_time
        else:
            # Convert timedelta to time
            total_seconds = int(departure_time.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            flight_time = time(hours, minutes, seconds)
        
        flight_datetime = datetime.combine(flight['departure_date'], flight_time)
        if flight_datetime <= datetime.now():
            flash('Cannot purchase tickets for past flights.', 'error')
            return redirect(url_for('search_flights'))
        
        # Check seat availability
        available_seats = flight['num_seats'] - flight['tickets_sold']
        if available_seats <= 0:
            flash('No seats available for this flight.', 'error')
            return redirect(url_for('search_flights'))
        
        # Get payment info from form
        card_type = request.form.get('card_type')
        card_number = request.form.get('card_number')
        card_name = request.form.get('card_name')
        card_expiry_month = request.form.get('card_expiry_month')
        card_expiry_year = request.form.get('card_expiry_year')
        
        # Validate inputs
        if not all([card_type, card_number, card_name, card_expiry_month, card_expiry_year]):
            flash('Please fill in all payment information.', 'error')
            return redirect(url_for('purchase_ticket', airline=airline, flight_number=flight_number, 
                                  departure_date=departure_date, departure_time=departure_time))
        
        # Convert month/year to date (use first day of month for card expiry)
        card_expiry = date(int(card_expiry_year), int(card_expiry_month), 1)
        
        # Insert ticket
        purchase_query = """
            INSERT INTO Ticket (customer_email, flight_airline, flight_number, 
                              flight_departure_date, flight_departure_time,
                              card_type, card_number, card_name, card_expiry, 
                              purchase_date, purchase_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), CURTIME())
        """
        
        result = execute_prepared_query(purchase_query, 
            (session['username'], airline, flight_number, departure_date, departure_time,
             card_type, card_number, card_name, card_expiry), fetch=False)
        
        if result is not None:
            flash('Ticket purchased successfully!', 'success')
            return redirect(url_for('customer_home'))
        else:
            flash('Purchase failed. Please try again.', 'error')
    
    # GET request - show purchase form
    flight_query = """
        SELECT f.*, a1.city as departure_city, a2.city as arrival_city,
               a.num_seats,
               (SELECT COUNT(*) FROM Ticket t 
                WHERE t.flight_airline = f.airline_name 
                AND t.flight_number = f.flight_number
                AND t.flight_departure_date = f.departure_date
                AND t.flight_departure_time = f.departure_time) as tickets_sold
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        JOIN Airplane a ON f.airline_name = a.airline_name AND f.airplane_id = a.id_number
        WHERE f.airline_name = %s AND f.flight_number = %s 
        AND f.departure_date = %s AND f.departure_time = %s
    """
    flight = execute_prepared_query(flight_query, (airline, flight_number, departure_date, departure_time))
    
    if not flight:
        flash('Flight not found.', 'error')
        return redirect(url_for('search_flights'))
    
    flight = flight[0]
    available_seats = flight['num_seats'] - flight['tickets_sold']
    
    return render_template('purchase_ticket.html', flight=flight, available_seats=available_seats)

@app.route('/customer/reviews', methods=['GET', 'POST'])
@require_customer_login
def customer_reviews():
    """View and add reviews for past flights"""
    if request.method == 'POST':
        # Add new review
        flight_airline = request.form.get('flight_airline')
        flight_number = int(request.form.get('flight_number'))
        flight_departure_date = request.form.get('flight_departure_date')
        flight_departure_time = request.form.get('flight_departure_time')
        rating = int(request.form.get('rating'))
        comment = request.form.get('comment', '')
        
        # Verify customer purchased this flight and it's in the past
        verify_query = """
            SELECT t.*, f.departure_date, f.departure_time
            FROM Ticket t
            JOIN Flight f ON t.flight_airline = f.airline_name 
                AND t.flight_number = f.flight_number
                AND t.flight_departure_date = f.departure_date
                AND t.flight_departure_time = f.departure_time
            WHERE t.customer_email = %s
                AND t.flight_airline = %s
                AND t.flight_number = %s
                AND t.flight_departure_date = %s
                AND t.flight_departure_time = %s
                AND CONCAT(f.departure_date, ' ', f.departure_time) <= NOW()
        """
        verification = execute_prepared_query(verify_query, 
            (session['username'], flight_airline, flight_number, flight_departure_date, flight_departure_time))
        
        if not verification:
            flash('You can only review flights you have purchased and that have already occurred.', 'error')
            return redirect(url_for('customer_reviews'))
        
        # Check if review already exists
        existing_query = """
            SELECT * FROM Review 
            WHERE customer_email = %s
                AND flight_airline = %s
                AND flight_number = %s
                AND flight_departure_date = %s
                AND flight_departure_time = %s
        """
        existing = execute_prepared_query(existing_query,
            (session['username'], flight_airline, flight_number, flight_departure_date, flight_departure_time))
        
        if existing:
            # Update existing review
            update_query = """
                UPDATE Review 
                SET rating = %s, comment = %s
                WHERE customer_email = %s
                    AND flight_airline = %s
                    AND flight_number = %s
                    AND flight_departure_date = %s
                    AND flight_departure_time = %s
            """
            execute_prepared_query(update_query,
                (rating, comment, session['username'], flight_airline, flight_number, 
                 flight_departure_date, flight_departure_time), fetch=False)
            flash('Review updated successfully!', 'success')
        else:
            # Insert new review
            insert_query = """
                INSERT INTO Review (customer_email, flight_airline, flight_number,
                                 flight_departure_date, flight_departure_time, rating, comment)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            execute_prepared_query(insert_query,
                (session['username'], flight_airline, flight_number, 
                 flight_departure_date, flight_departure_time, rating, comment), fetch=False)
            flash('Review submitted successfully!', 'success')
        
        return redirect(url_for('customer_reviews'))
    
    # GET request - show past flights that can be reviewed
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.arrival_date, f.arrival_time,
               a1.city as departure_city, a2.city as arrival_city,
               r.rating, r.comment
        FROM Ticket t
        JOIN Flight f ON t.flight_airline = f.airline_name 
            AND t.flight_number = f.flight_number
            AND t.flight_departure_date = f.departure_date
            AND t.flight_departure_time = f.departure_time
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        LEFT JOIN Review r ON t.customer_email = r.customer_email
            AND t.flight_airline = r.flight_airline
            AND t.flight_number = r.flight_number
            AND t.flight_departure_date = r.flight_departure_date
            AND t.flight_departure_time = r.flight_departure_time
        WHERE t.customer_email = %s
            AND CONCAT(f.departure_date, ' ', f.departure_time) <= NOW()
        ORDER BY f.departure_date DESC, f.departure_time DESC
    """
    
    flights = execute_prepared_query(query, (session['username'],))
    return render_template('customer_reviews.html', flights=flights or [])

# ============================================================================
# AIRLINE STAFF ROUTES
# ============================================================================

# Old staff routes redirect to unified login/register
@app.route('/staff/register', methods=['GET', 'POST'])
def staff_register():
    """Redirect to unified registration"""
    return redirect(url_for('register'))

@app.route('/staff/login', methods=['GET', 'POST'])
def staff_login():
    """Redirect to unified login"""
    return redirect(url_for('login'))

@app.route('/staff/home')
@require_staff_login
def staff_home():
    """Staff home page - View flights (default: next 30 days)"""
    # Default: show future flights for next 30 days
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.arrival_date, f.arrival_time, f.base_price, f.status,
               a1.city as departure_city, a2.city as arrival_city,
               (SELECT COUNT(*) FROM Ticket t 
                WHERE t.flight_airline = f.airline_name 
                AND t.flight_number = f.flight_number
                AND t.flight_departure_date = f.departure_date
                AND t.flight_departure_time = f.departure_time) as tickets_sold
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE f.airline_name = %s
            AND f.departure_date >= CURDATE()
            AND f.departure_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        ORDER BY f.departure_date, f.departure_time
    """
    
    flights = execute_prepared_query(query, (session['airline_name'],))
    return render_template('staff_home.html', flights=flights or [])

@app.route('/staff/flights', methods=['GET', 'POST'])
@require_staff_login
def staff_view_flights():
    """View flights with filtering options"""
    if request.method == 'POST':
        start_date = request.form.get('start_date', '')
        end_date = request.form.get('end_date', '')
        source = request.form.get('source', '')
        destination = request.form.get('destination', '')
        flight_type = request.form.get('flight_type', 'future')  # future, past, all
        
        # Build query
        query = """
            SELECT f.airline_name, f.flight_number, f.departure_airport, 
                   f.departure_date, f.departure_time, f.arrival_airport,
                   f.arrival_date, f.arrival_time, f.base_price, f.status,
                   a1.city as departure_city, a2.city as arrival_city,
                   (SELECT COUNT(*) FROM Ticket t 
                    WHERE t.flight_airline = f.airline_name 
                    AND t.flight_number = f.flight_number
                    AND t.flight_departure_date = f.departure_date
                    AND t.flight_departure_time = f.departure_time) as tickets_sold
            FROM Flight f
            JOIN Airport a1 ON f.departure_airport = a1.airport_code
            JOIN Airport a2 ON f.arrival_airport = a2.airport_code
            WHERE f.airline_name = %s
        """
        params = [session['airline_name']]
        
        # Filter by date range
        if flight_type == 'future':
            query += " AND CONCAT(f.departure_date, ' ', f.departure_time) > NOW()"
        elif flight_type == 'past':
            query += " AND CONCAT(f.departure_date, ' ', f.departure_time) <= NOW()"
        # 'all' shows everything, no additional filter
        
        if start_date:
            query += " AND f.departure_date >= %s"
            params.append(start_date)
        
        if end_date:
            query += " AND f.departure_date <= %s"
            params.append(end_date)
        
        if source:
            query += " AND (f.departure_airport = %s OR a1.city LIKE %s)"
            params.extend([source, f'%{source}%'])
        
        if destination:
            query += " AND (f.arrival_airport = %s OR a2.city LIKE %s)"
            params.extend([destination, f'%{destination}%'])
        
        query += " ORDER BY f.departure_date, f.departure_time"
        
        flights = execute_prepared_query(query, params)
        
        return render_template('staff_view_flights.html', flights=flights or [], 
                             start_date=start_date, end_date=end_date,
                             source=source, destination=destination, flight_type=flight_type)
    
    # Default: show future flights for next 30 days
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.arrival_date, f.arrival_time, f.base_price, f.status,
               a1.city as departure_city, a2.city as arrival_city,
               (SELECT COUNT(*) FROM Ticket t 
                WHERE t.flight_airline = f.airline_name 
                AND t.flight_number = f.flight_number
                AND t.flight_departure_date = f.departure_date
                AND t.flight_departure_time = f.departure_time) as tickets_sold
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE f.airline_name = %s
            AND f.departure_date >= CURDATE()
            AND f.departure_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        ORDER BY f.departure_date, f.departure_time
    """
    
    flights = execute_prepared_query(query, (session['airline_name'],))
    return render_template('staff_view_flights.html', flights=flights or [], 
                         start_date='', end_date='', source='', destination='', flight_type='future')

@app.route('/staff/flights/<airline>/<int:flight_number>/<departure_date>/<departure_time>/customers')
@require_staff_login
def staff_view_customers(airline, flight_number, departure_date, departure_time):
    """View all customers of a particular flight"""
    # Verify staff works for this airline
    if airline != session['airline_name']:
        flash('You can only view customers for flights of your airline.', 'error')
        return redirect(url_for('staff_view_flights'))
    
    query = """
        SELECT t.ticket_id, t.customer_email, t.purchase_date, t.purchase_time,
               c.name, c.phone_number, c.passport_number
        FROM Ticket t
        JOIN Customer c ON t.customer_email = c.customer_email
        WHERE t.flight_airline = %s
            AND t.flight_number = %s
            AND t.flight_departure_date = %s
            AND t.flight_departure_time = %s
        ORDER BY t.purchase_date DESC, t.purchase_time DESC
    """
    
    customers = execute_prepared_query(query, (airline, flight_number, departure_date, departure_time))
    
    # Get flight details
    flight_query = """
        SELECT f.*, a1.city as departure_city, a2.city as arrival_city
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE f.airline_name = %s AND f.flight_number = %s 
        AND f.departure_date = %s AND f.departure_time = %s
    """
    flight = execute_prepared_query(flight_query, (airline, flight_number, departure_date, departure_time))
    
    return render_template('staff_view_customers.html', 
                         customers=customers or [], 
                         flight=flight[0] if flight else None)

@app.route('/staff/flights/create', methods=['GET', 'POST'])
@require_staff_login
def staff_create_flight():
    """Create a new flight"""
    if request.method == 'POST':
        flight_number = request.form.get('flight_number')
        departure_airport = request.form.get('departure_airport')
        departure_date = request.form.get('departure_date')
        departure_time = request.form.get('departure_time')
        arrival_airport = request.form.get('arrival_airport')
        arrival_date = request.form.get('arrival_date')
        arrival_time = request.form.get('arrival_time')
        base_price = request.form.get('base_price')
        airplane_id = request.form.get('airplane_id')
        
        # Validate inputs
        if not all([flight_number, departure_airport, departure_date, departure_time,
                   arrival_airport, arrival_date, arrival_time, base_price, airplane_id]):
            flash('Please fill in all required fields.', 'error')
            airports = execute_prepared_query("SELECT airport_code, city FROM Airport")
            airplanes = execute_prepared_query(
                "SELECT id_number FROM Airplane WHERE airline_name = %s", 
                (session['airline_name'],))
            return render_template('staff_create_flight.html', 
                                 airports=airports or [], airplanes=airplanes or [])
        
        # Verify airplane belongs to this airline
        airplane_check = execute_prepared_query(
            "SELECT id_number FROM Airplane WHERE airline_name = %s AND id_number = %s",
            (session['airline_name'], airplane_id))
        if not airplane_check:
            flash('Invalid airplane ID for your airline.', 'error')
            airports = execute_prepared_query("SELECT airport_code, city FROM Airport")
            airplanes = execute_prepared_query(
                "SELECT id_number FROM Airplane WHERE airline_name = %s", 
                (session['airline_name'],))
            return render_template('staff_create_flight.html', 
                                 airports=airports or [], airplanes=airplanes or [])
        
        # Check if flight already exists
        check_query = """
            SELECT * FROM Flight 
            WHERE airline_name = %s AND flight_number = %s 
            AND departure_date = %s AND departure_time = %s
        """
        existing = execute_prepared_query(check_query, 
            (session['airline_name'], flight_number, departure_date, departure_time))
        
        if existing:
            flash('A flight with this number, date, and time already exists.', 'error')
            airports = execute_prepared_query("SELECT airport_code, city FROM Airport")
            airplanes = execute_prepared_query(
                "SELECT id_number FROM Airplane WHERE airline_name = %s", 
                (session['airline_name'],))
            return render_template('staff_create_flight.html', 
                                 airports=airports or [], airplanes=airplanes or [])
        
        # Insert new flight
        insert_query = """
            INSERT INTO Flight (airline_name, flight_number, departure_airport, 
                              departure_date, departure_time, arrival_airport,
                              arrival_date, arrival_time, base_price, status, airplane_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'on-time', %s)
        """
        
        result = execute_prepared_query(insert_query,
            (session['airline_name'], flight_number, departure_airport, departure_date, 
             departure_time, arrival_airport, arrival_date, arrival_time, base_price, airplane_id),
            fetch=False)
        
        if result is not None:
            flash('Flight created successfully!', 'success')
            return redirect(url_for('staff_home'))
        else:
            flash('Failed to create flight. Please try again.', 'error')
    
    # GET request - show form
    airports = execute_prepared_query("SELECT airport_code, city FROM Airport")
    airplanes = execute_prepared_query(
        "SELECT id_number FROM Airplane WHERE airline_name = %s", 
        (session['airline_name'],))
    return render_template('staff_create_flight.html', 
                         airports=airports or [], airplanes=airplanes or [])

@app.route('/staff/flights/change_status', methods=['GET', 'POST'])
@require_staff_login
def staff_change_status():
    """Change flight status"""
    if request.method == 'POST':
        airline = request.form.get('airline')
        flight_number = request.form.get('flight_number')
        departure_date = request.form.get('departure_date')
        departure_time = request.form.get('departure_time')
        new_status = request.form.get('status')
        
        # Verify staff works for this airline
        if airline != session['airline_name']:
            flash('You can only change status for flights of your airline.', 'error')
            return redirect(url_for('staff_change_status'))
        
        # Validate status
        if new_status not in ['on-time', 'delayed']:
            flash('Invalid status.', 'error')
            return redirect(url_for('staff_change_status'))
        
        # Update status
        update_query = """
            UPDATE Flight 
            SET status = %s
            WHERE airline_name = %s AND flight_number = %s 
            AND departure_date = %s AND departure_time = %s
        """
        
        result = execute_prepared_query(update_query,
            (new_status, airline, flight_number, departure_date, departure_time), fetch=False)
        
        if result is not None:
            flash(f'Flight status changed to {new_status} successfully!', 'success')
        else:
            flash('Failed to change status. Please try again.', 'error')
        
        return redirect(url_for('staff_change_status'))
    
    # GET request - show form with flights
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               f.status, a1.city as departure_city, a2.city as arrival_city
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE f.airline_name = %s
        ORDER BY f.departure_date DESC, f.departure_time DESC
    """
    
    flights = execute_prepared_query(query, (session['airline_name'],))
    return render_template('staff_change_status.html', flights=flights or [])

@app.route('/staff/airplanes/add', methods=['GET', 'POST'])
@require_staff_login
def staff_add_airplane():
    """Add a new airplane"""
    if request.method == 'POST':
        id_number = request.form.get('id_number')
        num_seats = request.form.get('num_seats')
        manufacturer = request.form.get('manufacturer')
        age = request.form.get('age')
        
        # Validate inputs
        if not all([id_number, num_seats, manufacturer, age]):
            flash('Please fill in all required fields.', 'error')
            airplanes = execute_prepared_query(
                "SELECT * FROM Airplane WHERE airline_name = %s ORDER BY id_number",
                (session['airline_name'],))
            return render_template('staff_add_airplane.html', airplanes=airplanes or [])
        
        # Check if airplane already exists
        check_query = """
            SELECT * FROM Airplane 
            WHERE airline_name = %s AND id_number = %s
        """
        existing = execute_prepared_query(check_query, (session['airline_name'], id_number))
        
        if existing:
            flash('An airplane with this ID already exists for your airline.', 'error')
            airplanes = execute_prepared_query(
                "SELECT * FROM Airplane WHERE airline_name = %s ORDER BY id_number",
                (session['airline_name'],))
            return render_template('staff_add_airplane.html', airplanes=airplanes or [])
        
        # Insert new airplane
        insert_query = """
            INSERT INTO Airplane (airline_name, id_number, num_seats, manufacturer, age)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        result = execute_prepared_query(insert_query,
            (session['airline_name'], id_number, num_seats, manufacturer, age), fetch=False)
        
        if result is not None:
            flash('Airplane added successfully!', 'success')
            # Show all airplanes for confirmation
            return redirect(url_for('staff_add_airplane'))
        else:
            flash('Failed to add airplane. Please try again.', 'error')
            airplanes = execute_prepared_query(
                "SELECT * FROM Airplane WHERE airline_name = %s ORDER BY id_number",
                (session['airline_name'],))
            return render_template('staff_add_airplane.html', airplanes=airplanes or [])
    
    # GET request - show form and all airplanes
    airplanes = execute_prepared_query(
        "SELECT * FROM Airplane WHERE airline_name = %s ORDER BY id_number",
        (session['airline_name'],))
    return render_template('staff_add_airplane.html', airplanes=airplanes or [])

@app.route('/staff/ratings')
@require_staff_login
def staff_view_ratings():
    """View flight ratings and comments"""
    query = """
        SELECT f.airline_name, f.flight_number, f.departure_airport, 
               f.departure_date, f.departure_time, f.arrival_airport,
               a1.city as departure_city, a2.city as arrival_city,
               AVG(r.rating) as avg_rating,
               COUNT(r.rating) as num_reviews
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        LEFT JOIN Review r ON f.airline_name = r.flight_airline
            AND f.flight_number = r.flight_number
            AND f.departure_date = r.flight_departure_date
            AND f.departure_time = r.flight_departure_time
        WHERE f.airline_name = %s
        GROUP BY f.airline_name, f.flight_number, f.departure_date, f.departure_time
        ORDER BY f.departure_date DESC, f.departure_time DESC
    """
    
    flights = execute_prepared_query(query, (session['airline_name'],))
    return render_template('staff_view_ratings.html', flights=flights or [])

@app.route('/staff/ratings/<airline>/<int:flight_number>/<departure_date>/<departure_time>')
@require_staff_login
def staff_view_flight_reviews(airline, flight_number, departure_date, departure_time):
    """View all reviews for a specific flight"""
    # Verify staff works for this airline
    if airline != session['airline_name']:
        flash('You can only view reviews for flights of your airline.', 'error')
        return redirect(url_for('staff_view_ratings'))
    
    # Get flight details
    flight_query = """
        SELECT f.*, a1.city as departure_city, a2.city as arrival_city
        FROM Flight f
        JOIN Airport a1 ON f.departure_airport = a1.airport_code
        JOIN Airport a2 ON f.arrival_airport = a2.airport_code
        WHERE f.airline_name = %s AND f.flight_number = %s 
        AND f.departure_date = %s AND f.departure_time = %s
    """
    flight = execute_prepared_query(flight_query, (airline, flight_number, departure_date, departure_time))
    
    # Get all reviews
    reviews_query = """
        SELECT r.*, c.name as customer_name
        FROM Review r
        JOIN Customer c ON r.customer_email = c.customer_email
        WHERE r.flight_airline = %s AND r.flight_number = %s 
        AND r.flight_departure_date = %s AND r.flight_departure_time = %s
        ORDER BY r.rating DESC
    """
    reviews = execute_prepared_query(reviews_query, (airline, flight_number, departure_date, departure_time))
    
    # Calculate average rating
    avg_rating = None
    if reviews:
        total = sum(r['rating'] for r in reviews)
        avg_rating = round(total / len(reviews), 2)
    
    return render_template('staff_view_flight_reviews.html', 
                         flight=flight[0] if flight else None,
                         reviews=reviews or [],
                         avg_rating=avg_rating)

@app.route('/staff/reports', methods=['GET', 'POST'])
@require_staff_login
def staff_view_reports():
    """View ticket sales reports"""
    if request.method == 'POST':
        report_type = request.form.get('report_type')  # 'date_range', 'last_month', 'last_year'
        start_date = request.form.get('start_date', '')
        end_date = request.form.get('end_date', '')
        
        # Build query based on report type
        if report_type == 'last_month':
            query = """
                SELECT DATE(t.purchase_date) as purchase_date, COUNT(*) as tickets_sold,
                       SUM(f.base_price) as total_revenue
                FROM Ticket t
                JOIN Flight f ON t.flight_airline = f.airline_name 
                    AND t.flight_number = f.flight_number
                    AND t.flight_departure_date = f.departure_date
                    AND t.flight_departure_time = f.departure_time
                WHERE t.flight_airline = %s
                    AND t.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
                GROUP BY DATE(t.purchase_date)
                ORDER BY purchase_date
            """
            params = [session['airline_name']]
        elif report_type == 'last_year':
            query = """
                SELECT MONTH(t.purchase_date) as month, YEAR(t.purchase_date) as year,
                       COUNT(*) as tickets_sold, SUM(f.base_price) as total_revenue
                FROM Ticket t
                JOIN Flight f ON t.flight_airline = f.airline_name 
                    AND t.flight_number = f.flight_number
                    AND t.flight_departure_date = f.departure_date
                    AND t.flight_departure_time = f.departure_time
                WHERE t.flight_airline = %s
                    AND t.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
                GROUP BY MONTH(t.purchase_date), YEAR(t.purchase_date)
                ORDER BY year, month
            """
            params = [session['airline_name']]
        else:  # date_range
            if not start_date or not end_date:
                flash('Please provide both start and end dates.', 'error')
                return redirect(url_for('staff_view_reports'))
            query = """
                SELECT DATE(t.purchase_date) as purchase_date, COUNT(*) as tickets_sold,
                       SUM(f.base_price) as total_revenue
                FROM Ticket t
                JOIN Flight f ON t.flight_airline = f.airline_name 
                    AND t.flight_number = f.flight_number
                    AND t.flight_departure_date = f.departure_date
                    AND t.flight_departure_time = f.departure_time
                WHERE t.flight_airline = %s
                    AND t.purchase_date >= %s AND t.purchase_date <= %s
                GROUP BY DATE(t.purchase_date)
                ORDER BY purchase_date
            """
            params = [session['airline_name'], start_date, end_date]
        
        report_data = execute_prepared_query(query, params)
        
        # Calculate totals
        total_tickets = sum(row['tickets_sold'] for row in report_data) if report_data else 0
        total_revenue = sum(float(row['total_revenue'] or 0) for row in report_data) if report_data else 0
        
        return render_template('staff_view_reports.html', 
                             report_data=report_data or [],
                             report_type=report_type,
                             start_date=start_date,
                             end_date=end_date,
                             total_tickets=total_tickets,
                             total_revenue=total_revenue)
    
    # GET request - show form
    return render_template('staff_view_reports.html', 
                         report_data=[],
                         report_type='',
                         start_date='',
                         end_date='',
                         total_tickets=0,
                         total_revenue=0)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
