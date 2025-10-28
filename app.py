from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",  # replace with your MySQL password
    database="college_events"
)
cursor = db.cursor(dictionary=True)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Student/Staff login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    dob_str = request.form['password']

    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
    except ValueError:
        return "Incorrect DOB format. Use yyyy-mm-dd."

    # Check students
    cursor.execute("SELECT * FROM students WHERE id=%s AND dob=%s", (username, dob))
    student = cursor.fetchone()

    # Check staff if not found in students
    if not student:
        cursor.execute("SELECT * FROM staff WHERE id=%s AND dob=%s", (username, dob))
        student = cursor.fetchone()

    if student:
        return render_template('student_home.html')
    else:
        return "Login failed. Please check your ID and DOB."

# Hoster login
@app.route('/host_login', methods=['POST'])
def host_login():
    username = request.form['username']
    dob_str = request.form['password']

    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
    except ValueError:
        return "Incorrect DOB format. Use yyyy-mm-dd."

    cursor.execute("SELECT * FROM hosters WHERE id=%s AND dob=%s", (username, dob))
    hoster = cursor.fetchone()

    if hoster:
        return render_template('hoster_home.html')
    else:
        return "Login failed. Only approved hosters can login."

# Student dashboard
@app.route('/student_home')
def student_home():
    return render_template('student_home.html')

# Hoster dashboard
@app.route('/hoster_home')
def hoster_home():
    return render_template('hoster_home.html')

# Host event page (only accessible from hoster dashboard)
@app.route('/hostevent')
def host_event():
    return render_template('hostevent.html')

# Post event
@app.route('/post_event', methods=['POST'])
def post_event():
    title = request.form['title']
    brochure = request.form['brochure']
    venue = request.form['venue']
    event_date = request.form['event_date']
    reg_link = request.form['reg_link']

    cursor.execute(
        "INSERT INTO events (title, brochure, venue, event_date, reg_link) VALUES (%s,%s,%s,%s,%s)",
        (title, brochure, venue, event_date, reg_link)
    )
    db.commit()
    return "Event posted successfully!"

if __name__ == '__main__':
    app.run(debug=True)


