"""
    File: 100476042_GUI_SOURCE_CODE.py

    Author: Hayden Jones

    Date started: 26/4/2025

    Description:
        Python file for the purpose of providing a graphical user interface for
        the user of the database. 
        Use of Psycopg2, to connect files to database
        Uses Tkinter.
        GUI to be used for transactions


    History: 26/4/2025 v 1.00

You can add an additional readme file (e.g., .txt) for proper setup and usage. (optional)
"""

#Imports
import psycopg2


#--------------- DATABASE CONNECTION ---------------#


# --- CREDENTIALS ---
#Setup connnection using credentials
def connect_to_database():

    #Attempts to connect to database with suitable output message
    try:
        conn = psycopg2.connect(
            host="cmpstudb-01.cmp.uea.ac.uk",
            dbname="bmd24dwu",
            user="bmd24dwu",
            password="AnyoneFamilyWelcome71?"
        )
        print("------ \n Connected to Database. \n------")
        return conn
    
    except psycopg2.Error as e:
        print("------ \n Error to Database:", e,"  \n------")
        exit(1)

# ------------------

#Executes SQL File 
def execute_SQL_file(conn, SQL_path):

    #Attempts to execute SQL file with suitable output message
    try:
        #Opens, reads and executes the SQL file
        with open (SQL_path, "r") as SQLFile:
            SQL = SQLFile.read()
        
        cur = conn.cursor()
        cur.execute(SQL)
        conn.commit()
        cur.close()
        print(f"------ \n Successfully executed file: {SQL_path} \n------")

    except Exception as e:
        print(f"------ \n Failed to execute file: {SQL_path},", e, "\n------")

#---------------------------------------------------#

def main():
    #Connects and executes following SQL files
    #Note: Data insert should always be executed after DDL
    conn = connect_to_database()
    execute_SQL_file(conn, "Upload Files/100476042_DDL.sql")
    execute_SQL_file(conn, "Upload Files/100476042_own_data.sql")
    conn.close()
    print("------ \n Disconnected from Database. \n------")

if __name__ == "__main__":
    main()