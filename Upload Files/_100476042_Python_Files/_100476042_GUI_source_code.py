"""
    File: 100476042_GUI_SOURCE_CODE.py

    Author: Hayden Jones

    Date started: 26/4/2025

    Description:
        Python file for the purpose of providing a graphical user interface for
        the user of the database. 
        Uses Tkinter.
        GUI to be used for transactions


    History: 26/4/2025 v 1.00

"""
import tkinter as tk
import tkinter.messagebox as messagebox

from _100476042_validation import *
from _100476042_db import set_current_user, add_student_to_db, add_exam_to_db, add_entry_to_db, delete_student_from_db, delete_exam_from_db, delete_entry_from_db

# ----------- GLOBAL STYLES -----------
LARGEFONT = ("Poppins", 28)
SMALLFONT = ("Poppins", 12)
font_1 = "Poppins"

# Colours
background_colour_1 = '#224855'
background_colour_2 = '#FFFFFF'
button_colour = '#90AEAD'
font_colour_1 = '#000000'
font_colour_2 = '#FFFFFF'
font_colour_3 = '#808080'

# ----------- FUNCTIONS -----------
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg=font_colour_3)

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg=font_colour_1)

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg=font_colour_3)

    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)

# ----------- HEADER COMPONENT -----------
class HeaderBar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=background_colour_1)

        self.controller = controller

        # Username
        self.username_label = tk.Label(
            self,
            text='',
            font=(font_1, 10),
            bg=background_colour_1,
            fg=font_colour_2
        )

        # Exit button
        exit_button = tk.Button(
            self,
            text='❌',
            font=(font_1, 10),
            bg=background_colour_2,
            relief='flat',
            command=controller.destroy
        )

        exit_button.pack(side='right', padx=(10, 10), pady=10)
        self.username_label.pack(side='right', padx=(0, 10), pady=10)

    def update_username(self):
        user = self.controller.logged_in_user
        self.username_label.config(text=f'Logged in as: {user}' if user else '')


# ----------- APP CLASS -----------
class CMP_Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CMPS Examinations")
        self.geometry('960x540')
        self.configure(bg=background_colour_1)
        self.resizable(True, True)

        self.logged_in_user = None

        # Frame container
        container = tk.Frame(self, bg=background_colour_1)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, MenuPage, StudentPage, ExamPage, EntryPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        self.frames[cont].tkraise()
        if hasattr(self.frames[cont], 'header'):
            self.frames[cont].header.update_username()
    

# ----------- LOGIN PAGE -----------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=background_colour_1)

        # Configure grid for centering
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        login_frame = tk.Frame(
            self,
            bg=background_colour_2,
            width=400,
            height=250,
            bd=2,
            relief='ridge',
            highlightthickness=2,
            highlightcolor='#dddddd'
        )
        login_frame.grid(row=0, column=0)
        login_frame.grid_columnconfigure(0, weight=1)

        def login():
            username = username_entry.get()
            if username and username != 'Username':
                print(f"Logging in as {username}")
                controller.logged_in_user= username
                controller.show_frame(MenuPage)
            else:
                print("Invalid username")
                messagebox.showerror('Login Error', 'Invalid Username')

        login_label = tk.Label(
            login_frame, text="Log in",
            bg=background_colour_2,
            fg=font_colour_1,
            font=LARGEFONT
        )
        username_entry = tk.Entry(
            login_frame,
            font=SMALLFONT,
            width=30
        )
        add_placeholder(username_entry, "Username")

        login_button = tk.Button(
            login_frame,
            text="Log In",
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=login
        )
        exit_button = tk.Button(
            login_frame,
            text='Exit',
            bg=background_colour_2,
            fg=font_colour_3,
            font=(font_1, 10),
            relief='flat',
            command=controller.destroy
        )

        # Place login widgets
        login_label.grid(row=0, column=0, pady=(20, 10), sticky='ew')
        username_entry.grid(row=1, column=0, padx=20, pady=10, ipady=5, sticky='ew')
        login_button.grid(row=2, column=0, padx=20, pady=10, ipadx=10, ipady=5, sticky='ew')
        exit_button.grid(row=3, column=0, pady=(10, 20), sticky='ew')


# ----------- MENU PAGE -----------
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=background_colour_1)

        # Configure grid for centering
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Header bar
        self.header = HeaderBar(self, controller)
        self.header.grid(row=0, column=0, sticky='ne')

        menu_title_label = tk.Label(
            self,
            text="Main Menu",
            font=LARGEFONT,
            bg=background_colour_1,
            fg=font_colour_2
        )
        menu_title_label.grid(row=0, column=0, columnspan=2, pady=(40, 10))

        content_section = tk.Frame(
            self,
            bg=background_colour_2,
            width=700,
            height=450,
            bd=2,
            relief='ridge'
        )
        content_section.grid(row=1, column=0, sticky='n')
        content_section.grid_rowconfigure(0, weight=1)
        content_section.grid_columnconfigure(0, weight=1)

        # Labels
        manage_label = tk.Label(content_section, text='Manage', font=(font_1, 14), bg=background_colour_2, fg=font_colour_1)
        view_label = tk.Label(content_section, text='View', font=(font_1, 14), bg=background_colour_2, fg=font_colour_1)

        # Manage buttons
        manage_buttons = [
            tk.Button(content_section, text='Student', relief='flat', width=50, font=SMALLFONT, bg=button_colour, fg=font_colour_2, command=lambda: controller.show_frame(StudentPage)),
            tk.Button(content_section, text='Exams', relief='flat', width=50, font=SMALLFONT, bg=button_colour, fg=font_colour_2, command=lambda: controller.show_frame(ExamPage)),
            tk.Button(content_section, text='Entries', relief='flat', width=50, font=SMALLFONT, bg=button_colour, fg=font_colour_2, command=lambda: controller.show_frame(EntryPage))
        ]

        # Separator
        separator = tk.Frame(content_section, bg='#CCCCCC', height=2, width=400)

        # View buttons
        view_buttons = [
            tk.Button(content_section, text='Timetable', relief='flat', width=50, font=SMALLFONT, bg=button_colour, fg=font_colour_2),
            tk.Button(content_section, text='Results', relief='flat', width=50, font=SMALLFONT, bg=button_colour, fg=font_colour_2)
        ]

        # Place widgets
        manage_label.grid(row=0, column=0, pady=(20, 10))
        for i, btn in enumerate(manage_buttons, start=1):
            btn.grid(row=i, column=0, padx=20, pady=5)

        separator.grid(row=4, column=0, pady=(20, 5))

        view_label.grid(row=5, column=0, pady=(5, 5))
        for i, btn in enumerate(view_buttons, start=6):
            btn.grid(row=i, column=0, padx=20, pady=5)


# ----------- BASE FORM PAGE TEMPLATE -----------
class BaseFormPage(tk.Frame):
    def __init__(self, parent, controller, title):
        super().__init__(parent, bg=background_colour_1)
        self.controller = controller

        # Configure grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Header bar
        self.header = HeaderBar(self, controller)
        self.header.grid(row=0, column=0, sticky='ne')

        # Title
        title_label = tk.Label(
            self,
            text=title,
            font=LARGEFONT,
            bg=background_colour_1,
            fg=font_colour_2
        )

        # Left container (Add section)
        self.left_container = tk.Frame(
            self,
            bg=background_colour_2,
            width=400,
            height=400,
            bd=2,
            relief='ridge'
        )
        self.left_container.grid_rowconfigure(0, weight=1)
        self.left_container.grid_columnconfigure(0, weight=1)

        # Right container (Delete section)
        self.right_container = tk.Frame(
            self,
            bg=background_colour_2,
            width=400,
            height=400,
            bd=2,
            relief='ridge'
        )
        self.right_container.grid_rowconfigure(0, weight=1)
        self.right_container.grid_columnconfigure(0, weight=1)

        # Add section title
        self.add_label = tk.Label(
            self.left_container,
            text="Add",
            font=(font_1, 16),
            bg=background_colour_2,
            fg=font_colour_1
        )

        # Delete section title
        self.delete_label = tk.Label(
            self.right_container,
            text="Delete",
            font=(font_1, 16),
            bg=background_colour_2,
            fg=font_colour_1
        )

        # Widget Placement
        title_label.grid(row=0, column=0, columnspan=2, pady=(30, 10))
        self.left_container.grid(row=1, column=0, padx=40, pady=10, sticky='nsew')
        self.right_container.grid(row=1, column=1, padx=40, pady=10, sticky='nsew')
        self.add_label.grid(row=0, column=0, pady=(10, 5), sticky='w')
        self.delete_label.grid(row=0, column=0, pady=(10, 5), sticky='w')


#------------ MANAGE PAGES -----------#
# ----------- STUDENT PAGE -----------#
class StudentPage(BaseFormPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, title='StudentPage')

        # --- Add Section ---
        # Add form widgets to left container
        self.student_number_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.student_name_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.student_email_entry = tk.Entry(self.left_container, font=SMALLFONT)

        self.add_button = tk.Button(
            self.left_container,
            text='Add Student',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.add_student
        )

        add_placeholder(self.student_number_entry, "Student Number")
        add_placeholder(self.student_name_entry, 'Student Name')
        add_placeholder(self.student_email_entry, 'Student Email')

        # Widget Placement for left container
        self.student_number_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.student_name_entry.grid(row=2, column=0, padx=20, pady=5, sticky='ew')
        self.student_email_entry.grid(row=3, column=0, padx=20, pady=5, sticky='ew')
        self.add_button.grid(row=4, column=0, padx=20, pady=5, sticky='ew')

        # --- Delete Section ---
        # Add form widgets to right container
        self.delete_student_entry = tk.Entry(self.right_container, font=SMALLFONT)

        self.delete_button = tk.Button(
            self.right_container,
            text='Delete Student',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.delete_student
        )

        add_placeholder(self.delete_student_entry, "Student Number")
        
        # Widget Placement for right container
        self.delete_student_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.delete_button.grid(row=2, column=0, padx=20, pady=(10, 20), sticky='ew')

    # --- Functionality for Entries/Deletions ---
    def add_student(self):
        # Retrieving inputs
        sno = self.student_number_entry.get()
        sname = self.student_name_entry.get()
        semail = self.student_email_entry.get()

        # Validation
        errors = validate_student_data(sno, sname, semail)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = add_student_to_db(sno, sname, semail)

        if success:
            messagebox.showinfo("Success", "Student added successfully!")
            # Clears entry fields
            self.student_number_entry.delete
            self.student_name_entry.delete
            self.student_email_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)
        
    def delete_student(self):
        # Retrieving inputs
        sno = self.delete_student_entry.get()

        # Validation
        errors = validate_delete_student(sno)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = delete_student_from_db(sno)

        if success:
            messagebox.showinfo("Success", "Student deleted successfully!")
            # Clears entry fields
            self.delete_student_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)


# ----------- EXAM PAGE -----------#
class ExamPage(BaseFormPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, title='ExamPage')

        # --- Add Section ---
        # Add form widgets to left container
        self.exam_code_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_title_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_location_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_date_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_time_entry = tk.Entry(self.left_container, font=SMALLFONT)

        self.add_button = tk.Button(
            self.left_container,
            text='Add Exam',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.add_exam
        )

        add_placeholder(self.exam_code_entry, "Exam Code")
        add_placeholder(self.exam_title_entry, 'Exam Title')
        add_placeholder(self.exam_location_entry, 'Exam Location')
        add_placeholder(self.exam_date_entry, 'Exam Date, YYYY-MM-DD')
        add_placeholder(self.exam_time_entry, 'Exam Time, HH:MM')

        # Widget Placement for left container
        self.exam_code_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.exam_title_entry.grid(row=2, column=0, padx=20, pady=5, sticky='ew')
        self.exam_location_entry.grid(row=3, column=0, padx=20, pady=5, sticky='ew')
        self.exam_date_entry.grid(row=4, column=0, padx=20, pady=5, sticky='ew')
        self.exam_time_entry.grid(row=5, column=0, padx=20, pady=5, sticky='ew')
        self.add_button.grid(row=6, column=0, padx=20, pady=5, sticky='ew')

        # --- Delete Section ---
        # Add form widgets to right container
        self.delete_exam_entry = tk.Entry(self.right_container, font=SMALLFONT)

        self.delete_button = tk.Button(
            self.right_container,
            text='Delete Exam',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.delete_exam
        )

        add_placeholder(self.delete_exam_entry, "Exam Code")
        
        # Widget Placement for right container
        self.delete_exam_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.delete_button.grid(row=2, column=0, padx=20, pady=(10, 20), sticky='ew')


    # --- Functionality for Entries/Deletions ---
    def add_exam(self):
        # Retrieving inputs
        excode = self.exam_code_entry.get()
        extitle = self.exam_title_entry.get()
        exlocation = self.exam_location_entry.get()
        exdate = self.exam_date_entry.get()
        extime = self.exam_time_entry.get()

        # Validation
        errors = validate_exam_data(excode, extitle, exlocation, exdate, extime)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = add_exam_to_db(excode, extitle, exlocation, exdate, extime)

        if success:
            messagebox.showinfo("Success", "Exam added successfully!")
            # Clears entry fields
            self.exam_code_entry.delete
            self.exam_title_entry.delete
            self.exam_location_entry.delete
            self.exam_date_entry.delete
            self.exam_time_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)
        
    def delete_exam(self):
        # Retrieving inputs
        excode = self.delete_exam_entry.get()

        # Validation
        errors = validate_delete_exam(excode)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = delete_exam_from_db(excode)

        if success:
            messagebox.showinfo("Success", "Exam deleted successfully!")
            # Clears entry fields
            self.delete_exam_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)


# ----------- ENTRY PAGE -----------#
class EntryPage(BaseFormPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, title='EntryPage')

        # --- Add Section ---
        # Add form widgets to left container
        self.entry_number_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_code_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.student_number_entry = tk.Entry(self.left_container, font=SMALLFONT)
        self.exam_grade_entry = tk.Entry(self.left_container, font=SMALLFONT)

        self.add_button = tk.Button(
            self.left_container,
            text='Add Entry',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.add_entry
        )

        add_placeholder(self.entry_number_entry, "Entry Number")
        add_placeholder(self.exam_code_entry, 'Exam Code')
        add_placeholder(self.student_number_entry, 'Student Number')
        add_placeholder(self.exam_grade_entry, 'Exam Grade')

        # Widget Placement for left container
        self.entry_number_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.exam_code_entry.grid(row=2, column=0, padx=20, pady=5, sticky='ew')
        self.student_number_entry.grid(row=3, column=0, padx=20, pady=5, sticky='ew')
        self.exam_grade_entry.grid(row=4, column=0, padx=20, pady=5, sticky='ew')
        self.add_button.grid(row=5, column=0, padx=20, pady=5, sticky='ew')

        # --- Delete Section ---
        # Add form widgets to right container
        self.delete_entry_entry = tk.Entry(self.right_container, font=SMALLFONT)

        self.delete_button = tk.Button(
            self.right_container,
            text='Delete Entry',
            bg=button_colour,
            fg=font_colour_2,
            font=SMALLFONT,
            relief='flat',
            command=self.delete_entry
        )

        add_placeholder(self.delete_exam_entry, "Entry Number")
        
        # Widget Placement for right container
        self.delete_entry_entry.grid(row=1, column=0, padx=20, pady=5, sticky='ew')
        self.delete_button.grid(row=2, column=0, padx=20, pady=(10, 20), sticky='ew')

    # --- Functionality for Entries/Deletions ---
    def add_entry(self):
        # Retrieving inputs
        eno = self.entry_number_entry.get()
        excode = self.exam_code_entry.get()
        sno = self.student_number_entry.get()
        egrade = self.exam_grade_entry.get()

        # Validation
        errors = validate_entry_data(eno, excode, sno, egrade)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = add_entry_to_db(eno, excode, sno, egrade)
        if success:
            messagebox.showinfo("Success", "Entry added successfully!")
            # Clears entry fields
            self.entry_number_entry.delete
            self.exam_code_entry.delete
            self.student_number_entry.delete
            self.exam_grade_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)
        
    def delete_entry(self):
        # Retrieving inputs
        eno = self.delete_entry_entry.get()

        # Validation
        errors = validate_delete_entry(eno)

        if errors:
            messagebox.showerror("Input Errors", "\n".join(errors))
            return
        
        # Check if runs on database
        success, database_error = delete_entry_from_db(eno)

        if success:
            messagebox.showinfo("Success", "Entry deleted successfully!")
            # Clears entry fields
            self.delete_entry_entry.delete
        else:
            messagebox.showerror("Database Error", database_error)

# ----------- RUN APP -----------
if __name__ == "__main__":
    app = CMP_Application()
    app.mainloop()
