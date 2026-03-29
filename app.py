from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50)
        )
    """)

    cursor.execute("INSERT INTO users (name) VALUES ('Hello User')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    return f"Database Connected Successfully! Data: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)