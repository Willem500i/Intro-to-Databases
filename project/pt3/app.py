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
            return redirect(url_for('customer_login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/')
def index():
    """Home page - shows different content based on login status"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def customer_register():
    """Customer registration"""
    if request.method == 'POST':
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
            return redirect(url_for('customer_login'))
        
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
            return redirect(url_for('customer_login'))
        else:
            flash('Registration failed. Please try again.', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def customer_login():
    """Customer login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Hash password using MD5 as specified in requirements
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        query = "SELECT customer_email, name FROM Customer WHERE customer_email = %s AND password = %s"
        user = execute_prepared_query(query, (email, password_hash))
        
        if user:
            session['user_type'] = 'customer'
            session['username'] = user[0]['customer_email']
            session['name'] = user[0]['name']
            flash('Login successful!', 'success')
            return redirect(url_for('customer_home'))
        else:
            flash('Invalid email or password.', 'error')
    
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
