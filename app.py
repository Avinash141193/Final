from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import csv
import os

# ---------------- INIT ----------------
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ensures correct path for Render

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect(os.path.join(BASE_DIR, "students.db"))
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll TEXT,
            attendance REAL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            english INTEGER,
            maths INTEGER,
            physics INTEGER,
            chemistry INTEGER,
            biology INTEGER,
            computer INTEGER,
            total INTEGER,
            result TEXT,
            grade TEXT
        )
    """)

    conn.commit()
    conn.close()

# ---------------- IMPORT CSV ----------------
def import_students_from_csv():
    csv_path = os.path.join(BASE_DIR, "students.csv")
    conn = get_db()
    cur = conn.cursor()

    count = cur.execute("SELECT COUNT(*) FROM students").fetchone()[0]

    if count == 0 and os.path.exists(csv_path):
        with open(csv_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Insert student
                cur.execute(
                    "INSERT INTO students (name, roll, attendance) VALUES (?, ?, ?)",
                    (row["name"], row["roll"], float(row["attendance"]))
                )
                student_id = cur.lastrowid

                # If marks exist in CSV, insert marks
                if all(k in row for k in ["english", "maths", "physics", "chemistry", "biology", "computer"]):
                    marks_list = [
                        int(row["english"]),
                        int(row["maths"]),
                        int(row["physics"]),
                        int(row["chemistry"]),
                        int(row["biology"]),
                        int(row["computer"])
                    ]
                    total = sum(marks_list)
                    result, grade = calculate_result_and_grade(marks_list)
                    cur.execute("""
                        INSERT INTO marks
                        (student_id, english, maths, physics, chemistry, biology, computer, total, result, grade)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (student_id, *marks_list, total, result, grade))

    conn.commit()
    conn.close()

# ---------------- GRADE LOGIC ----------------
def calculate_result_and_grade(marks):
    if any(m < 35 for m in marks):
        return "Fail", "F"
    avg = sum(marks) / len(marks)
    if avg >= 75:
        return "Pass", "A"
    elif avg >= 50:
        return "Pass", "B"
    else:
        return "Pass", "C"

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    search = request.args.get("search")
    conn = get_db()
    query = """
        SELECT students.*, marks.id AS mark_id
        FROM students
        LEFT JOIN marks ON students.id = marks.student_id
    """
    if search:
        query += " WHERE students.name LIKE ? OR students.roll LIKE ?"
        students = conn.execute(query, ('%' + search + '%', '%' + search + '%')).fetchall()
    else:
        students = conn.execute(query).fetchall()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]
        total_days = int(request.form["total_days"])
        attended_days = int(request.form["attended_days"])
        attendance = (attended_days / total_days) * 100

        conn = get_db()
        existing = conn.execute("SELECT * FROM students WHERE roll = ?", (roll,)).fetchone()
        if existing:
            conn.close()
            return render_template("add_student.html", error="Roll number already exists!")
        conn.execute("INSERT INTO students (name, roll, attendance) VALUES (?, ?, ?)",
                     (name, roll, attendance))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add_student.html")

@app.route("/add_marks/<int:student_id>", methods=["GET", "POST"])
def add_marks(student_id):
    conn = get_db()
    existing = conn.execute("SELECT * FROM marks WHERE student_id = ?", (student_id,)).fetchone()
    if request.method == "POST":
        english = int(request.form["english"])
        maths = int(request.form["maths"])
        physics = int(request.form["physics"])
        chemistry = int(request.form["chemistry"])
        biology = int(request.form["biology"])
        computer = int(request.form["computer"])
        marks_list = [english, maths, physics, chemistry, biology, computer]
        total = sum(marks_list)
        result, grade = calculate_result_and_grade(marks_list)

        if existing:
            conn.execute("""
                UPDATE marks SET
                english=?, maths=?, physics=?, chemistry=?, biology=?, computer=?,
                total=?, result=?, grade=?
                WHERE student_id=?
            """, (*marks_list, total, result, grade, student_id))
        else:
            conn.execute("""
                INSERT INTO marks
                (student_id, english, maths, physics, chemistry, biology, computer,
                 total, result, grade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (student_id, *marks_list, total, result, grade))
        conn.commit()
        conn.close()
        return redirect("/view/" + str(student_id))
    conn.close()
    return render_template("add_marks.html", marks=existing)

@app.route("/view/<int:student_id>")
def view_student(student_id):
    conn = get_db()
    student = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    marks = conn.execute("SELECT * FROM marks WHERE student_id = ?", (student_id,)).fetchone()
    conn.close()
    return render_template("view_student.html", student=student, marks=marks)

@app.route("/delete_student/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_db()
    conn.execute("DELETE FROM marks WHERE student_id = ?", (student_id,))
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return redirect("/")

# ---------------- INITIALIZE ----------------
# Run this **once on startup**, also works with Gunicorn
create_tables()
import_students_from_csv()
