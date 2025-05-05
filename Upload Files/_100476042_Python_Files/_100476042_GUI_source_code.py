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
import tkinter as tk
import tkinter as tk

# ----------- GLOBAL STYLES -----------
LARGEFONT = ("Poppins", 28)
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


# ----------- APP CLASS -----------
class CMP_Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CMPS Examinations")
        self.geometry('960x540')
        self.configure(bg=background_colour_1)
        self.resizable(True, True)


        # Frame container
        container = tk.Frame(self, bg=background_colour_1)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, MenuPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        self.frames[cont].tkraise()


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
            if username != 'Username':
                print(f"Logging in as {username}")
                controller.show_frame(MenuPage)
            else:
                print("Invalid username")

        login_label = tk.Label(
            login_frame, text="Log in",
            bg=background_colour_2,
            fg=font_colour_1,
            font=LARGEFONT
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
            tk.Button(content_section, text='Student', relief='flat', width=50, font=(font_1, 12), bg=button_colour, fg=font_colour_2),
            tk.Button(content_section, text='Exams', relief='flat', width=50, font=(font_1, 12), bg=button_colour, fg=font_colour_2),
            tk.Button(content_section, text='Entries', relief='flat', width=50, font=(font_1, 12), bg=button_colour, fg=font_colour_2)
        ]

        # Separator
        separator = tk.Frame(content_section, bg='#CCCCCC', height=2, width=400)

        # View buttons
        view_buttons = [
            tk.Button(content_section, text='Timetable', relief='flat', width=50, font=(font_1, 12), bg=button_colour, fg=font_colour_2),
            tk.Button(content_section, text='Results', relief='flat', width=50, font=(font_1, 12), bg=button_colour, fg=font_colour_2)
        ]

        # Place widgets
        manage_label.grid(row=0, column=0, pady=(20, 10))
        for i, btn in enumerate(manage_buttons, start=1):
            btn.grid(row=i, column=0, padx=20, pady=5)

        separator.grid(row=4, column=0, pady=(20, 5))

        view_label.grid(row=5, column=0, pady=(5, 5))
        for i, btn in enumerate(view_buttons, start=6):
            btn.grid(row=i, column=0, padx=20, pady=5)


# ----------- RUN APP -----------
if __name__ == "__main__":
    app = CMP_Application()
    app.mainloop()
