# Grade 10 Student Management System

#### Video Demo: https://youtu.be/KpQIl_28XTo?feature=shared

#### Description:
The Grade 10 Student Management System is a web-based application developed as my final project for CS50x 2025. The goal of this project is to provide a simple yet functional platform for managing student academic records, including attendance, subject-wise marks, grades, and results. The application is designed for teachers or school administrators who want a lightweight system to manage student data without relying on complex external tools.

This project is built using Python (Flask) for the backend, SQLite for the database, and HTML/CSS for the frontend. The system supports full CRUD (Create, Read, Update, Delete) functionality for student records and demonstrates concepts taught throughout the CS50 course, such as database design, web development, server-side logic, and clean code organization.

The application provides the following features:
•	Add new students with name, roll number, and attendance percentage
•	Automatically calculate attendance based on total working days and attended days
•	Add subject-wise marks for each student
•	Subjects include English, Maths, Physics, Chemistry, Biology, and Computer Science
•	Automatically calculate:
   o	Total marks
      o	Pass/Fail result
         o	Grade (A, B, C, or F)
         •	View detailed student reports with:
            o	Individual subject marks
               o	Total marks
                  o	Grade and result
                  •	Delete students along with their associated marks
                  •	Search students by name or roll number
                  •	Optional CSV import to preload student and marks data
                  •	Clean and simple user interface styled with CSS


                  #### File Structure:
                  grade10_student_system/
                  │
                  ├── app.py
                  ├── students.db
                  ├── students.csv
                  ├── templates/
                  │   ├── index.html
                  │   ├── add_student.html
                  │   ├── add_marks.html
                  │   └── view_student.html
                  └── static/
                      └── style.css

                      #### File Descriptions

                      **app.py**
                      This file contains the core logic of the application. It initializes the Flask app, manages database connections, defines all routes, and handles form submissions. It includes logic for adding students, calculating attendance, inserting and retrieving marks, determining pass/fail status, assigning grades, importing data from CSV files, and deleting student records. The grading logic ensures that if a student fails any subject, they are marked as failed overall.

                      **students.db**
                      This SQLite database stores all persistent data for the application. It contains two tables: `students` and `marks`. The students table stores basic student information such as name, roll number, and attendance percentage. The marks table stores subject-wise marks, total marks, result, and grade, linked to students through a foreign key relationship.

                      **students.csv**
                      This CSV file is used to preload student data into the database when the application is run for the first time. This feature was added to demonstrate file handling and automated data insertion. It makes testing easier and simulates how schools may import existing data into a system.

                      **templates/**
                      This folder contains all HTML templates used by Flask. Each template corresponds to a route and uses Jinja templating to dynamically display data retrieved from the database.

                      **static/style.css**
                      This file defines the styling of the web application. It improves the user experience by adding spacing, colors, table formatting, buttons, and card-style layouts to make the interface clean and readable.



                      #### Design Decisions:

                      •	Flask was chosen because it is lightweight, beginner-friendly, and aligns with CS50’s curriculum.
                      •	SQLite was selected for simplicity and ease of use without requiring a separate database server.
                      •	Marks and students were separated into different tables to maintain good database normalization.
                      •	CSV import was added as a practical enhancement to demonstrate file handling and automation.
                      •	CSS was intentionally kept simple to ensure clarity and usability without overcomplicating the UI.

                      #### How to Run the Project

                      •	Ensure Python 3 is installed
                      •	Navigate to the project directory
                      •	Run the application:  python app.py
                      •	After running the application, open a browser and visit http://127.0.0.1:5000

                      This project was fully designed and implemented by me as part of the CS50x final project. While general documentation and course materials were referenced, all application logic, database design, routes, templates, and styling were written by me specifically for this project.

                      #### Challenges and Learning Outcomes

                      One of the main challenges in this project was designing a database structure that could efficiently store both student information and their subject marks while maintaining proper relationships. Separating students and marks into different tables helped avoid redundancy but required careful handling of foreign keys and queries.

                      Another challenge was ensuring that grades and results were calculated correctly. I implemented logic to automatically fail a student if any subject mark was below the passing threshold, which required validating input and handling edge cases.

                      Handling CSV imports also presented challenges, particularly ensuring the correct column names and data types. Debugging database errors helped me better understand SQLite operations and error handling.

                      Through this project, I gained confidence in Flask routing, template rendering, SQL queries, and debugging runtime errors. I also improved my understanding of how frontend and backend components interact in a real web application.

                      #### Future Improvements

                      If extended further, this project could include authentication for teachers, support for multiple classes or grades, exporting reports as PDF files, and improved user interface design using Bootstrap. These enhancements would make the system more scalable and suitable for real-world school environments.


                      #### Conclusion
                      The Grade 10 Student Management System demonstrates my understanding of full-stack web development, database management, and software design principles learned throughout CS50. This project reflects my ability to plan, implement, debug, and enhance a real-world application from scratch. Overall, this project allowed me to combine concepts from multiple weeks of CS50, including Python, SQL, Flask, HTML, and CSS, into a complete and functional application.
