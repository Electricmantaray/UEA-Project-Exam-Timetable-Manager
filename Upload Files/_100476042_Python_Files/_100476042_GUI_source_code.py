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
    #--- Colours and Fonts ---#
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
    container.grid(row=0, column=0)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)


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
    #login_frame.grid_propagate(False)
    # Configure grid
    login_frame.grid_columnconfigure(0, weight=1) 
    

    # Menu Frame
    menu_frame = tk.Frame(
        container, 
        bg=background_colour_1,
        )


    #--- Sub-section Frames ---#
    
    # Content section
    content_section = tk.Frame(
        menu_frame,
        bg=background_colour_2,
        width=700,
        height=450,
        bd=2,
        relief='ridge'
        )
    content_section.grid_rowconfigure(1, weight=1)
    content_section.grid_columnconfigure(0, weight=1)

    

    # Place and ordering 
    for frame in (menu_frame, login_frame):
        frame.grid(row=0, column=0)
    login_frame.tkraise()


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
        command=lambda: login())
    
    exit_button = tk.Button(
        login_frame, 
        text='Exit', 
        bg=background_colour_2, 
        fg=font_colour_3, 
        font=(font_1, 10), 
        relief='flat', 
        command=window.destroy)
    

    #Placing widgets
    login_label.grid(row=0, column=0, pady=(20, 10), sticky='ew')
    username_entry.grid(row=1, column=0, padx=20, pady=10, ipady=5, sticky='ew')
    login_button.grid(row=2, column=0, padx=20, pady=10, ipadx=10, ipady=5, sticky='ew')
    exit_button.grid(row=3, column=0, pady=(10, 20), sticky='ew')
    #---------#



    #--- Menu Frame ---#

    # Creating widget
    # Title
    menu_title_label = tk.Label(
        menu_frame,
        text="Main Menu",
        font=(font_1, 28),
        bg=background_colour_1,
        fg=font_colour_2
    )


    # Manage
    manage_label = tk.Label(
        content_section,
        text='Manage',
        font=(font_1, 14),
        bg=background_colour_2,
        fg=font_colour_1
    )

    manage_button_1 = tk.Button(
        content_section,
        text='Student',
        relief='flat',
        width=50,
        font=(font_1, 12),
        bg=button_colour, 
        fg=font_colour_2, 
    ) 

    manage_button_2 = tk.Button(
        content_section,
        text='Exams',
        relief='flat',
        width=50,
        font=(font_1, 12),
        bg=button_colour, 
        fg=font_colour_2, 
    ) 

    manage_button_3 = tk.Button(
        content_section,
        text='Entries',
        relief='flat',
        width=50,
        font=(font_1, 12),
        bg=button_colour, 
        fg=font_colour_2, 
    ) 

    # Seperator
    seperator = tk.Frame(
        content_section,
        bg='#CCCCCC',
        height=2,
        width=400
        )


    # View
    view_label = tk.Label(
        content_section,
        text='View',
        font=(font_1, 14),
        bg=background_colour_2,
        fg=font_colour_1
    )

    view_button_1 = tk.Button(
        content_section,
        text='Timetable',
        relief='flat',
        width=50,
        font=(font_1, 12),
        bg=button_colour, 
        fg=font_colour_2, 
    ) 

    view_button_2 = tk.Button(
        content_section,
        text='Results',
        relief='flat',
        width=50,
        font=(font_1, 12),
        bg=button_colour, 
        fg=font_colour_2, 
    ) 

    # Placing Widgets

    menu_title_label.grid(row=0, column=0, columnspan=2, pady=(40,10), sticky='n')
    content_section.grid(row=1, column=0)

    manage_label.grid(row=0, column=0, pady=(20,10))
    manage_button_1.grid(row=1, column=0, padx=20, pady=5)
    manage_button_2.grid(row=2, column=0, padx=20, pady=5)
    manage_button_3.grid(row=3, column=0, padx=20, pady=5)

    seperator.grid(row=4, column=0, pady=(20, 5))

    view_label.grid(row=5, column=0, pady=(5, 5))
    view_button_1.grid(row=6, column=0, padx=20, pady=5)
    view_button_2.grid(row=7, column=0, padx=20, pady=(5, 20))

    #---------#


    window.mainloop()





















#-----------------------------------#