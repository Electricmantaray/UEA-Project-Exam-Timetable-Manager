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
def CMP_Application():
    #--- Variables ---#
    background_colour_1 = '#224855'
    background_colour_2 = '#FFFFFF'
    button_colour = '#90AEAD'
    font_colour_1 = '#000000'
    font_colour_2 = '#FFFFFF'
    font_colour_3 = '#808080'
 
    font_1 = 'Poppins'


    #--- Define root window ---#
    window = tk.Tk()
    window.title("CMPS Examinations")
    window.geometry('960x540')
    window.configure(bg= background_colour_1)
    window.resizable(True, True)
    

    #--- Container for "pages" ---#
    container = tk.Frame(
        window, 
        bg=background_colour_1
        )
    container.pack(fill='both', expand=True)


    #--- Frames ---#
    # Login Frame
    login_frame = tk.Frame(
        container, 
        bg=background_colour_2, 
        width=400, 
        height=250,
        bd=2,
        relief='ridge',
        highlightthickness=2,
        highlightcolor='#dddddd'
        )
    
    # Menu Frame
    menu_frame = tk.Frame(
        container, 
        bg=background_colour_2,
        width=500,
        height=300,
        bd=2,
        relief='ridge'
    )

    for frame in (menu_frame, login_frame):
        frame.place(relx=0.5, rely=0.5, anchor='center')
        
    
    






    #--- Functions ---#

    #--- Placeholder logic ---#
    def add_placeholder(entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(fg=font_colour_3)

        # On click placeholder is deleted
        def on_focus_in(event):
            if entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg=font_colour_1)
        
        # Placeholder replaced
        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder_text)
                entry.config(fg=font_colour_3)
        
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)

    #--- Login logic ---#
    def login():
        username = username_entry.get()
        # Prevents placeholder from being submitted
        if username != 'Username':
            print(f"Logging in as {username}")
            menu_frame.tkraise()
        else:
            print("Invalid username")





    #--- Login page ---#
    login_frame.grid_columnconfigure(1, weight=1)

    # Creating widgets  
    login_label = tk.Label(
        login_frame, text="Log in", 
        bg=background_colour_2, 
        fg=font_colour_1, 
        font=(font_1, 28)
        )
    
    username_entry = tk.Entry(
        login_frame, 
        font=(font_1, 12), 
        width=30
        )
    add_placeholder(username_entry, "Username")

    login_button = tk.Button(
        login_frame, 
        text="Log In", 
        bg=button_colour, 
        fg=font_colour_2, 
        font=(font_1, 12), 
        relief='flat', 
        command='login')
    
    exit_button = tk.Button(
        login_frame, 
        text='Exit', 
        bg=background_colour_2, 
        fg=font_colour_3, 
        font=(font_1, 10), 
        relief='flat', 
        command=window.destroy)
    

    #Placing widgets
    login_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky='ew')
    username_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10, ipady=5, sticky='ew')
    login_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10, ipadx=10, ipady=5, sticky='ew')
    exit_button.grid(row=3, column=0, columnspan=2, pady=(10, 20), sticky='ew')
    #---------#

    #--- Menu Frame ---#
    

    
    #---------#

    # Start app on login
    login_frame.tkraise
    window.mainloop()





















#-----------------------------------#