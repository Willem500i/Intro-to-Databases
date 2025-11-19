import os

class Config:
    # Database configuration
    # Railway provides these environment variables: MYSQLHOST, MYSQLPORT, MYSQLUSER, MYSQLPASSWORD, MYSQLDATABASE
    MYSQL_HOST = os.environ.get('MYSQLHOST') or os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_PORT = int(os.environ.get('MYSQLPORT') or os.environ.get('MYSQL_PORT') or 3306)
    MYSQL_USER = os.environ.get('MYSQLUSER') or os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQLPASSWORD') or os.environ.get('MYSQL_PASSWORD') or ''
    MYSQL_DATABASE = os.environ.get('MYSQLDATABASE') or os.environ.get('MYSQL_DATABASE') or 'airline_reservation'
    
    # Secret key for sessions (required for Flask sessions)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
