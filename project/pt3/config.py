import os
from urllib.parse import urlparse

class Config:
    # Database configuration
    # Support both Railway's MYSQL_URL and individual variables
    MYSQL_URL = os.environ.get('MYSQL_URL') or os.environ.get('MySQL.MYSQL_URL')
    
    # Debug: print what we're getting (remove in production)
    if not MYSQL_URL:
        print("WARNING: MYSQL_URL not found in environment variables")
        print(f"Available env vars with MYSQL: {[k for k in os.environ.keys() if 'MYSQL' in k.upper()]}")
    
    if MYSQL_URL:
        # Parse MySQL URL: mysql://user:password@host:port/database
        parsed = urlparse(MYSQL_URL)
        MYSQL_HOST = parsed.hostname or 'localhost'
        MYSQL_USER = parsed.username or 'root'
        MYSQL_PASSWORD = parsed.password or ''
        MYSQL_DATABASE = parsed.path.lstrip('/') if parsed.path else 'railway'
        MYSQL_PORT = parsed.port or 3306
    else:
        # Use individual environment variables (for local development)
        MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
        MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
        MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''
        MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'airline_reservation'
        MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    
    # Secret key for sessions (required for Flask sessions)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

