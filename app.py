from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)   # allow frontend requests

# -------------------------------
# Helper Functions for Scraping
# -------------------------------
def scrape_page(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def scrape_exam_schedule(year_keyword):
    url = "https://www.jeppiaarinstitute.org/exam.php"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    # Filter only lines containing the year keyword
    lines = [line for line in text.split("\n") if year_keyword.lower() in line.lower()]
    return "\n".join(lines) if lines else f"No schedule found for {year_keyword}"

# -------------------------------
# Sample Data (can be replaced with scraping)
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
    "Electronics and Communication Engineering",
    "Mechanical Engineering",
    "Computer Science and Business System",
    "Information Technology"
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
# Exam Schedule by Year (Scraping)
# -------------------------------
@app.route('/getExamScheduleFirstYear')
def get_exam_schedule_first_year():
    return jsonify({"first_year_exam": scrape_exam_schedule("First Year")})

@app.route('/getExamScheduleSecondYear')
def get_exam_schedule_second_year():
    return jsonify({"second_year_exam": scrape_exam_schedule("Second Year")})

@app.route('/getExamScheduleThirdYear')
def get_exam_schedule_third_year():
    return jsonify({"third_year_exam": scrape_exam_schedule("Third Year")})

@app.route('/getExamScheduleFourthYear')
def get_exam_schedule_fourth_year():
    return jsonify({"fourth_year_exam": scrape_exam_schedule("Fourth Year")})

# -------------------------------
# Parent Queries
# -------------------------------
@app.route('/getFees')
def get_fees():
    data = scrape_page("https://www.jeppiaarinstitute.org/fees.php")
    return jsonify({"fees": data})

@app.route('/getHostel')
def get_hostel():
    data = scrape_page("https://www.jeppiaarinstitute.org/hostel.php")
    return jsonify({"hostel": data})

@app.route('/getTransport')
def get_transport():
    data = scrape_page("https://www.jeppiaarinstitute.org/transport.php")
    return jsonify({"transport": data})

@app.route('/getParentSupport')
def get_parent_support():
    data = scrape_page("https://www.jeppiaarinstitute.org/support.php")
    return jsonify({"support": data})

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
