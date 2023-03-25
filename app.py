from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://basketball_db_user:2AotULLsHGewiAHNHCxZRgoU1OafHJpI@dpg-cgfku182qv28tc05hmj0-a/basketball_db")
    conn.close()
    return "Database Connection Successful"
