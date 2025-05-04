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
# --- CREDENTIALS ---
# Setup connnection using credentials
def connect_to_database():

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