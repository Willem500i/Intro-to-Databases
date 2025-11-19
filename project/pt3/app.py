from flask import Flask, render_template, request
from database import execute_prepared_query
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """Home page with flight search"""
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
