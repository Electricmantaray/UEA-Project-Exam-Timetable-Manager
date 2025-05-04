"""
    File: 100476042_main.py

    Author: Hayden Jones

    Date started: 30/4/2025

    Description:
        Runs the SQL scripts
        Launches the Tkinter GUI

    History: 30/4/2025 v 1.00

"""

#Imports
from _100476042_db import connect_to_database, execute_SQL_file
from _100476042_GUI_source_code import execute_CMP_Application
import tkinter as tk

#--------------- MAIN ---------------#

def main():
    # Connects and executes following SQL files
    conn = connect_to_database()
    execute_SQL_file(conn, "Upload Files/100476042_DDL.sql")
    execute_SQL_file(conn, "Upload Files/100476042_own_data.sql")
    conn.close()
    print("------ Disconnected from Database. ------")

    #Lanch the GUI
    execute_CMP_Application()


if __name__ == "__main__":
    main()


#------------------------------------#