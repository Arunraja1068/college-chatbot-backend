from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # allow frontend requests

# -------------------------------
# Sample Data (replace with scraping later)
# -------------------------------

exam_schedule_data = [
    "Semester Exams start on March 20",
    "Hall tickets available online from March 15"
]

events_data = [
    "Tech Fest on April 5",
    "Sports Day on April 12"
]

admissions_data = [
    "Admissions open for B.Tech AI & DS",
    "Last date to apply: May 30"
]

placements_data = [
    "Infosys campus drive on April 18",
    "TCS interviews scheduled for April 25"
]

departments_data = [
    "Computer Science and Engineering",
    "Artificial Intelligence and Data Science",
    "Electronics and Communication Engineering"
]

library_data = [
    "Library open from 8 AM to 8 PM",
    "Digital resources available via student portal"
]

# -------------------------------
# API Routes
# -------------------------------

@app.route('/')
def home():
    return "✅ College Chatbot Backend is Running!"

@app.route('/getExamSchedule')
def get_exam_schedule():
    return jsonify({"exam_schedule": exam_schedule_data})

@app.route('/getEvents')
def get_events():
    return jsonify({"events": events_data})

@app.route('/getAdmissions')
def get_admissions():
    return jsonify({"admissions": admissions_data})

@app.route('/getPlacements')
def get_placements():
    return jsonify({"placements": placements_data})

@app.route('/getDepartments')
def get_departments():
    return jsonify({"departments": departments_data})

@app.route('/getLibrary')
def get_library():
    return jsonify({"library": library_data})

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)