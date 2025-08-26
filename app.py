from flask import Flask, render_template, request, redirect
import pymysql
import config

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        db=config.MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )

def init_db():
    """Create tasks table if it doesn't exist"""
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                is_done BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    connection.commit()
    connection.close()

@app.route('/')
def index():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
        tasks = cursor.fetchall()
    connection.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    if title:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
        connection.commit()
        connection.close()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE tasks SET is_done = TRUE WHERE id = %s", (task_id,))
    connection.commit()
    connection.close()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    connection.commit()
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    print("Initializing database...")
    init_db()   # ✅ Ensure table exists before running app
    print("Starting Flask app...")
    app.run(debug=True, host='0.0.0.0', port=5000)
