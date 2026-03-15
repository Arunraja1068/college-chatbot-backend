from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)   # allow frontend requests

# -------------------------------
# Helper Function for Scraping
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
    """- Placement Rate: ~80–85% of B.Tech students
- Highest Package: ₹24 LPA
- Average Package: ~₹4.5 LPA
- Top Offers: Up to ₹10 LPA
- Key Recruiters: Amazon, TCS, Wipro, Google"""
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

admissions_eligibility = [
    """Regular Admission (First Year)
Pass 10+2 (Academic Stream) with Maths, Physics, Chemistry.
Or pass 10+2 (Vocational Stream – Engineering/Technology).

Lateral Entry (Direct to 3rd Semester)
Diploma in Engineering/Technology (Tamil Nadu State Board or equivalent).
Or B.Sc. (Maths as a subject) – must take 2 extra engineering subjects in 3rd & 4th semesters."""
]

scholarshi_data = [
    """- Govt. of Tamil Nadu Scholarships (BC/SC/ST students – PMSS, FG)
- Admission Scholarships
- 100% for cutoff >185 (Maths, Physics, Chemistry)
- Women Scholarship
- Sports Scholarship
- School Merit Scholarships
- +1/+2 students scoring >480 in SSLC/CBSE"""
]

fees_data = [
    """- Overall Fees (All Courses): ₹41,000 – ₹6 Lakhs
- UG Fees (B.Tech): ₹1.65 Lakhs – ₹2.2 Lakhs
- PG Fees (M.Tech/MBA): ₹41,000"""
]

hostel_data = [
    """- Separate hostels for boys & girls
- Spacious rooms with attached bath, hot/cold water
- Dining hall with steam cooking, mineral water, uninterrupted power & water
- Recreation halls with TV, reading room, computer room, gymnasium
- STD/ISD facilities, newspapers, assistant wardens for guidance
- Strict discipline rules, formal dress code, ragging prohibited"""
]

transport_data = [
    """- Fleet of 19 buses covering city & nearby areas
- Transport arranged for all students to ensure punctuality
- Extended service for special classes, placements, training, industry visits, NSS camps"""
]

# -------------------------------
# Syllabus Links (official website)
# -------------------------------
syllabus_links = {
    "cse": "https://www.jeppiaarinstitute.org/wp-content/uploads/2024/09/R2024-Curriculum-and-Syllabus-CSE.pdf",
    "it": "https://www.jeppiaarinstitute.org/wp-content/uploads/2025/07/Dept-of-IT-Curriculum-and-Syllabus_.pdf",
    "ai&ds": "https://www.jeppiaarinstitute.org/wp-content/uploads/2025/07/SYLLABUS-OF-AIDS-1.pdf",
    "ece": "https://www.jeppiaarinstitute.org/wp-content/uploads/2025/07/R2024-ECE-Updated-Syllabus-as-on-2.3.26-till-5th-Sem-1.pdf",
    "mech": "https://www.jeppiaarinstitute.org/wp-content/uploads/2024/09/R2024-Curriculum-and-Syllabus-Mechanical.pdf"
}

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

@app.route('/getAdmissionEligibility')
def get_admission_eligibility():
    return jsonify({"eligibility": admissions_eligibility})

@app.route('/getscholarshi')
def get_scholarshi():
    return jsonify({"scholarshi": scholarshi_data})

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
# Parent-Focused Queries
# -------------------------------
@app.route('/getFees')
def get_fees():
    return jsonify({"fees": fees_data})

@app.route('/getHostel')
def get_hostel():
    return jsonify({"hostel": hostel_data})

@app.route('/getTransport')
def get_transport():
    return jsonify({"transport": transport_data})

@app.route('/getParentSupport')
def get_parent_support():
    data = scrape_page("https://www.jeppiaarinstitute.org/support.php")
    return jsonify({"support": data})

# -------------------------------
# Syllabus Endpoint
# -------------------------------
@app.route('/getSyllabus/<course>')
def get_syllabus(course):
    link = syllabus_links.get(course.lower())
    if link:
        return jsonify({"syllabus_link": link})
    else:
        return jsonify({"error": f"No syllabus found for {course}"}), 404

# -------------------------------
# Run Server
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
