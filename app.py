from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
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
            name VARCHAR(50),
            email VARCHAR(50),
            course VARCHAR(50)
        )
    """)

    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        course = request.form['course']

        cursor.execute(
            "INSERT INTO users (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course)
        )
        conn.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    return render_template('index.html', data=data)

@app.route('/delete/<int:id>')
def delete(id):
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )

    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)