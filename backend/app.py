from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection details
DB_HOST = "postgres.backend.svc.cluster.local"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_NAME = "mydb"

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NOW();')
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"data": data[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

