
---
<p align="center">
<b>All data seen in demo is dummy data (fake) for demonstration purposes</b>
</p>

---

# Exam Timetable Manager (E.T.M)- UEA Module Coursework


[![Postgresql](https://img.shields.io/badge/postgresql-3670A0?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter%20-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)

## Purpose:

This project was created for my UEA Year 1 Databases module as a piece of individual coursework to demonstrate my ability with databases and PostgreSQL. The aim was to build a system to manage exam schedules for a professional membership society, keeping track of students, their exam entries, and ensuring no scheduling conflicts like students sitting multiple exams on the same day.

My task involved designing and implementing the database structure with all the necessary tables and constraints to maintain data integrity. I also had to write SQL queries to handle key operations such as adding students, entering exams, cancelling entries, and generating reports on exam timetables and results.

To make the system user-friendly, I developed a simple Python GUI so users could interact with the database without needing to write SQL commands. Overall, the project was about applying database concepts practically while meeting the requirements of the coursework.

---

# E.T.M

This software is intended to be used by exam adminstration when entering details regarding students exams, including both the creation and management of exams and entering the details of students partaking in them, using the constraints within the database fields to prevent incorrect information from being submitted and provides a exam data management tool.

---

## Tech Stack

| Layer         | Technology                          | Purpose                                                                  |
| ------------- | ----------------------------------- | ------------------------------------------------------------------------ |
| **Frontend**  | Tkinter (Python)                    | Simple graphical user interface for user interaction with the database   |
| **Backend**   | Python                              | Handles business logic and communicates between GUI and database         |
| **Database**  | PostgreSQL                          | Stores all exam, student, entry, and cancellation data with constraints  |
| **Testing**   | DML Test                            | Uses Transaction of Interest                                             |

---

## Demonstrations

### Login Page
https://github.com/user-attachments/assets/fbf48c09-9e15-470a-87d3-18670901a85f

---

### Main Menu
https://github.com/user-attachments/assets/959570b2-c204-4fd0-a636-aa282b371855

https://github.com/user-attachments/assets/1d8fed57-63d5-4337-b6a9-80553426ca55

---

### Student Page
https://github.com/user-attachments/assets/5181bf43-d1d3-4645-b99b-b3dc5f09dac1

---

### Exam Page
https://github.com/user-attachments/assets/f4e524bf-dcf1-4994-8516-9f9bcc3ea352

---

### Entry Page
https://github.com/user-attachments/assets/6ea36bbf-a30c-4867-a0ff-adce52c31d0c

---

### Timetable Views
https://github.com/user-attachments/assets/172181ea-ab29-43c9-8e62-6b52d360bbbe

---

### Results View
https://github.com/user-attachments/assets/a618c36b-6d51-41e5-9e47-83cc26fb21ad

---

## Project Structure

<details open>
  <summary><b>File Structure</b></summary>

```

📁 UEA-Project-Exam-Timetable-Manager
├── 📁 Upload Files
│   ├── 📁 _100476042_Python_Files         # Python source and module files
│   │   ├── __init__.py                     # Package initializer
│   │   ├── _100476042_db.py                # Database interaction code
│   │   ├── _100476042_GUI_source_code.py  # GUI implementation and event handling
│   │   ├── _100476042_main.py              # Main program entry point
│   │   └── _100476042_validation.py       # Validation logic and helper functions
│   │
│   ├── 100476042_assessment_template.doc  # Assessment submission template (MS Word)
│   ├── 100476042_DDL.sql                   # SQL Data Definition Language script
│   ├── 100476042_DML.sql                   # SQL Data Manipulation Language script
│   ├── 100476042_own_data.sql              # Custom SQL data inserts or modifications
│   └── 100476042_README.txt                # Plain text project readme and notes
│
└── README.md                               # Project root README with overview and instructions

```

