"""
    File: 100476042_db.py

    Author: Hayden Jones

    Date started: 26/4/2025

    Description:
        Use of Psycopg2, to connect files to database
        Executes all SQL files


    History: 26/4/2025 v 1.00

"""

#Imports
import psycopg2

#--------------- DATABASE CONNECTION ---------------#

# Global variables
# Connection
conn = None
# Username
current_user = 'User'

# --- CREDENTIALS ---
# Setup connnection using credentials
def connect_to_database():
    # Connects if theres no connection
    global conn
    if conn is None:
        # Attempts to connect to database with suitable output message
        print("Connecting to Database ...")
        
        try:
            conn = psycopg2.connect(
                host="cmpstudb-01.cmp.uea.ac.uk",
                dbname="bmd24dwu",
                user="bmd24dwu",
                password="AnyoneFamilyWelcome71?"
            )
            print("------ Connected to Database. ------")
            return conn
        
        except psycopg2.Error as e:
            print("------  Error connecting to Database: ------", e)
            exit(1)
    return conn

# Closes connection and resets variable
def disconnect_from_database():
    global conn
    if conn:
        conn.close()
        print("------ Disconnected from Database. ------")
        conn = None

# ------------------

# Executes SQL File 
def execute_SQL_file(conn, SQL_path):

    # Attempts to execute SQL file with suitable output message
    try:
        # Opens, reads and executes the SQL file
        with open (SQL_path, "r") as SQLFile:
            SQL = SQLFile.read()
        
        cur = conn.cursor()
        cur.execute(SQL)
        conn.commit()
        cur.close()
        print(f"- Successfully executed file: {SQL_path}")

    except Exception as e:
        print(f"- Failed to execute file: {SQL_path},", e)
#---------------------------------------------------#

#--------------- ADD/DELETE FROM GUI ---------------#

# --- Username ---
#Use for cancel table
def set_current_user(username: str):
    global current_user
    current_user = username

# --- Student ---
def add_student_to_db(sno: int, sname: str, semail: str):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Inserts student
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO student(sno, sname, semail) VALUES (%s, %s, %s);",
            (sno, sname, semail)
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Added student: {sno}, {sname}, {semail}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error adding student:', e)
        return False, str(e)

def delete_student_from_db(sno: int):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Deletes student
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM student WHERE sno = %s;",
            (sno, )
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Deleted student: {sno}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error deleting student:', e)
        return False, str(e)

# --- Exam ---
def add_exam_to_db(excode: str, extitle: str, exlocation: str, exdate: str, extime: str):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Inserts exam
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO exam(excode, extitle, exlocation, exdate, extime) VALUES (%s, %s, %s, %s, %s);",
            (excode, extitle, exlocation, exdate, extime)
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Added exam: {excode}, {extitle}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error adding exam:', e)
        return False, str(e)

def delete_exam_from_db(excode: str):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Deletes exam
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM exam WHERE excode = %s;",
            (excode, )
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Deleted exam: {excode}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error deleting exam:', e)
        return False, str(e)

# --- Entry ---
def add_entry_to_db(eno: int, excode: str, sno: int, egrade):
    # If connected then just returns global variable
    conn = connect_to_database()

    if egrade == '':
        egrade = None
    
    try:
        #Inserts entry
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO entry(eno, excode, sno, egrade) VALUES (%s, %s, %s, %s);",
            (eno, excode, sno, egrade)
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Added entry: {eno}, {excode}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error adding entry:', e)
        return False, str(e)

def delete_entry_from_db(eno):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Deletes entry
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM entry WHERE eno = (%s);",
            (eno, )
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Deleted exam: {eno}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error deleting exam:', e)
        return False, str(e)

def update_entry_to_db(eno: int, egrade):
    # If connected then just returns global variable
    conn = connect_to_database()

    if egrade == '':
        egrade = None

    try:
        #Inserts entry
        cur = conn.cursor()
        cur.execute(
            "UPDATE entry SET egrade = %s WHERE eno = %s;",
            (egrade, eno)
        )
        conn.commit()
        cur.close

        print(f'{current_user} | Updated entry: {eno}, {egrade}')
        return True, None
    
    except psycopg2.Error as e:
        # If an error occurs, roll back the transaction to prevent blocking future operations
        conn.rollback()
        print(f'{current_user} | Error adding entry:', e)
        return False, str(e)
#---------------------------------------------------#

#--------------- VIEW FROM GUI ---------------#
def fetch_timetable_from_db(sno):
    # If connected then just returns global variable
    conn = connect_to_database()

    try:
        #Deletes entry
        cur = conn.cursor()

        cur.execute(
            "SELECT sname, excode, extitle, exlocation, exdate, extime FROM student_timetable WHERE sno = %s;",
            (sno, )
        )
        data = cur.fetchall()
        conn.commit()
        cur.close

        print(f'{current_user} | Fetched Timetable: {sno}')
        return data, None
    
    except psycopg2.Error as e:
            # If an error occurs, roll back the transaction to prevent blocking future operations
            conn.rollback()
            print(f'{current_user} | Error Fetching Timetable:', e)


#---------------------------------------------#