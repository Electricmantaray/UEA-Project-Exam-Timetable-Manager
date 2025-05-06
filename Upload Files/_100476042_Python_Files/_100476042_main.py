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
from _100476042_db import connect_to_database,disconnect_from_database, execute_SQL_file
from _100476042_GUI_source_code import CMP_Application


#--------------- MAIN ---------------#

def on_closing(app):
    disconnect_from_database()
    app.destroy()

def main():
    # Connects and executes following SQL files
    conn = connect_to_database()

    execute_SQL_file(conn, "Upload Files/100476042_DDL.sql")
    execute_SQL_file(conn, "Upload Files/100476042_own_data.sql")

    #Lanch the GUI
    app = CMP_Application()

    # Upon Gui close it disconnects database
    app.protocol("WM_DELETE_WINDOW", lambda: on_closing(app))
    app.mainloop()


if __name__ == "__main__":
    main()


#------------------------------------#