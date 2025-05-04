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

"""

#Imports
import tkinter as tk

#--------------- GUI ---------------#

## Initialise
def execute_CMP_Application():
    

    # Define root window
    window = tk.Tk()
    window.title("CMPS Examinations")
    window.geometry('340x440')
    window.configure(bg='#224855')


    window.mainloop()

#-----------------------------------#