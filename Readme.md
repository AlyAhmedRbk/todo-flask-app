# 📝 Flask To-Do App

A simple **Flask + MySQL To-Do List Application** that lets you add, complete, and delete tasks.  
This project is great for learning **Flask**, **MySQL integration**, and can be extended with Docker for deployment.

---

## 🚀 Features
- Add tasks with a title  
- Mark tasks as completed (`is_done = TRUE`)  
- Delete tasks from the list  
- Auto-creates the `tasks` table if it doesn’t exist  
- Lightweight and easy to run locally  

---

## 📂 Project Structure
.
├── app.py # Flask application
├── templates/ # HTML templates (index.html)
├── config.py # MySQL credentials
├── requirements.txt
└── README.md

## ⚙️ Requirements
- Python **3.10+**
- MySQL server
- pip (Python package manager)

---

## 🔧 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app
```

2. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure database

Create a config.py file in the project root:

MYSQL_HOST = "localhost"
MYSQL_USER = "your_mysql_user"
MYSQL_PASSWORD = "your_mysql_password"
MYSQL_DB = "your_database_name"


Create the database:

mysql -u root -p -e "CREATE DATABASE your_database_name;"

5. Run the Flask app
python app.py


The app will be running at 👉 http://localhost:5000

🐳 Run with Docker (Optional)

To containerize the app:

# Build the Docker image
docker build -t flask-todo-app .

# Run the container
docker run -d -p 5000:5000 --name todo-app flask-todo-app

📜 Useful MySQL CLI Commands

Check table structure:

mysql -u root -p -D your_database_name -e "DESCRIBE tasks;"


Insert a task manually:

mysql -u root -p -D your_database_name -e "INSERT INTO tasks (title) VALUES ('Learn Flask');"


View all tasks:

mysql -u root -p -D your_database_name -e "SELECT * FROM tasks;"

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request. 🚀
