"""
    File: 100476042_validation.py

    Author: Hayden Jones

    Date started: 30/4/2025

    Description:
        validates access level inputs

    History: 30/4/2025 v 1.00

"""
from datetime import datetime

#--------------- USERNAME VALIDATION ---------------#
def validate_username(username):
    errors = []

    if (not username) or (len(username.strip()) == 0) or len(username) > 200:
        errors.append('Username cannot be empty or above 200 characters.')

    return errors

#--------------- STUDENT VALIDATION ---------------#

def validate_student_data(sno, sname, semail):
    errors = []

    # sno: integer, PK
    try:
        sno = int(sno)
        if not isinstance(sno, int):
            errors.append("Student number must be an integer")
    except ValueError:
        errors.append("Student number must be an integer")

    # sname: <200 characters, Not Null
    if (not sname or len(sname.strip()) == 0) or len(sname) > 200:
        errors.append("Student name cannot be empty or above 200 characters.")

    # semail: <200 characters, valid format, Not Null
    if (not semail) or (len(semail.strip()) == 0) or ('@' not in semail) or (len(sname) > 200):
        errors.append('Invalid email')

    return errors
#--------------- EXAM VALIDATION ---------------#

def validate_exam_data(excode, extitle, exlocation, exdate, extime):
    errors = []

    # excode: 4 characters, PK
    if (not isinstance(excode, str)) or (len(excode) != 4):
        errors.append("Exam code must be exactly 4 characters.")

    # extitle: <200 characters, Not Null
    if (not extitle) or (len(extitle.strip()) == 0) or (len(extitle) > 200):
        errors.append("Exam title cannot be empty or above 200 characters.")

    # exlocation: <200 characters, Not Null
    if (not exlocation) or (len(exlocation.strip()) == 0) or (len(exlocation) > 200):
        errors.append("Exam location cannot be empty or above 200 characters.")

    # exdate: valid format, within check range, Not Null
    try:
        exdate = datetime.strptime(exdate, "%Y-%m-%d").date()
        if not (datetime(2025, 11, 1).date() <= exdate <= datetime(2025, 11, 30).date()):
            errors.append("Exam date must be between 2025-11-01 and 2025-11-30.")
    except ValueError:
        errors.append("Exam date must be in YYYY-MM-DD format.")

    # extime: valid time, within check range, Not Null
    try:
        extime = datetime.strptime(extime, "%H:%M").time()
        if not (datetime.strptime("09:00", "%H:%M").time() <= extime <= datetime.strptime("18:00", "%H:%M").time()):
            errors.append("Exam time must be between 09:00 and 18:00.")
    except ValueError:
        errors.append("Exam time must be in HH:MM format.")


    return errors

#--------------- ENTRY VALIDATION ---------------#

def validate_entry_data(eno, excode, sno, egrade):
    errors = []

    # eno: integer, PK
    try:
        eno = int(eno)
        if not isinstance(eno, int):
            errors.append("Entry number must be an integer.")
    except ValueError:
        errors.append("Entry number must be an integer.")
    

    # excode: 4 characters, Not Null
    if (not isinstance(excode, str)) or (len(excode) != 4):
        errors.append("Exam code must be exactly 4 characters.")

    # sno: integer, Not Null
    try:
        sno = int(sno)
        if not isinstance(sno, int):
            errors.append("Student number must be an integer")
    except ValueError:
        errors.append("Student number must be an integer")

def validate_update_entry_data(eno, egrade):
    errors = []

        # eno: integer, PK
    try:
        eno = int(eno)
        if not isinstance(eno, int):
            errors.append("Entry number must be an integer.")
    except ValueError:
        errors.append("Entry number must be an integer.")
    

    # egrade: decimal, between 0-100
    try:
        egrade = float(egrade)
        if not (0 <= egrade <= 100):
            errors.append("Grade must be between 0 and 100.")
    except ValueError:
        errors.append("Grade must be number")

    return errors

#--------------- DELETION VALIDATION ---------------#

def validate_delete_student(sno):
    errors = []

    # sno: integer
    try:
        sno = int(sno)
        if not isinstance(sno, int):
            errors.append("Student number must be an integer")
    except ValueError:
        errors.append("Student number must be an integer")
    
    return errors

def validate_delete_exam(excode):
    errors = []

    # excode: 4 characters, Not Null
    if (not isinstance(excode, str)) or (len(excode) != 4):
        errors.append("Exam code must be exactly 4 characters.")
    
    return errors

def validate_delete_entry(eno):
    errors = []

    # eno: integer
    try:
        eno = int(eno)
        if not isinstance(eno, int):
            errors.append("Entry number must be an integer.")
    except ValueError:
        errors.append("Entry number must be an integer.")

    return errors

