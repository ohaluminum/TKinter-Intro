import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Account.employee_login_db import EmployeeLoginDB
from Account.admin_login_db import AdminLoginDB

# Reference: Tkinter Application to Switch Between Different Page Frames - https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# Database context
employeeLoginDB = EmployeeLoginDB()
adminLoginDB = AdminLoginDB()


# Application Class
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Configure the application properties 
        self.title("Soundbox Dance Studios")
        self.iconbitmap("logo_ico.ico")
        self.geometry("1100x650")

        # Creating a container
        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")    # container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing an empty frame array
        self.frames = {}

        for F in (Homepage, Login, Register):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Display the current page
        self.show_frame(Homepage)
    
    def show_frame(self, curr):
        frame = self.frames[curr]
        frame.tkraise()

    def run(self):
        self.mainloop()


# Homepage Window
class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        # Create home page element
        self.knugenLogo = ImageTk.PhotoImage((Image.open("logo_png.png")))
        self.logoLabel = tk.Label(self, image=self.knugenLogo).pack()
        self.header = tk.Label(self, text="Soundbox Dance Studios", font=("Segoe UI", 18, "bold")).pack()    # The first parameter: where to put the element

        # Login button
        tk.Label(self, text="").pack()    # Equivalent to empty line 
        self.loginButton = tk.Button(self, text="Login", height="2", width="15", command=lambda: controller.show_frame(Login)).pack()
        
        # Register button
        tk.Label(self, text="").pack()    # Equivalent to empty line
        self.registerButton = tk.Button(self, text="Register", height="2", width="15", command=lambda: controller.show_frame(Register)).pack()


# Login Window
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create login page element
        tk.Label(self, text="").grid(row=0, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        self.header = tk.Label(self, text="User Login", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, columnspan=5)   # The first parameter: where to put the element

        self.userType = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Username Entry
        tk.Label(self, text="").grid(row=3, column=0)    # Equivalent to empty line
        self.usernameLabel = tk.Label(self, text="Enter Username: ", font=("Segoe UI", 11)).grid(row=4, column=0, sticky=tk.W, columnspan=3)
        self.usernameEntry = tk.Entry(self, textvariable=self.username)
        self.usernameEntry.grid(row=4, column=3, sticky=tk.W, columnspan=2)

        # Password Entry
        self.passwordLabel = tk.Label(self, text="Enter Password: ", font=("Segoe UI", 11)).grid(row=5, column=0, sticky=tk.W, columnspan=3)
        self.passwordEntry = tk.Entry(self, textvariable=self.password)
        self.passwordEntry.grid(row=5, column=3, columnspan=2)
        
        # Role Selection
        tk.Label(self, text="").grid(row=6, column=0)    # Equivalent to empty line
        self.adminRadioButton = tk.Radiobutton(self, text="Administrator", variable=self.userType, value="Admin", font=("Segoe UI", 11)).grid(row=7, column=0, sticky=tk.W, columnspan=3)
        self.employeeRadioButton = tk.Radiobutton(self, text="Employee", variable=self.userType, value="Employee", font=("Segoe UI", 11)).grid(row=7, column=3, sticky=tk.E, columnspan=2)
        
        # Submit Button
        tk.Label(self, text="").grid(row=8, column=0, columnspan=2)    # Equivalent to empty line
        self.submitButton = tk.Button(self, text="Login", height="2", width="35", command=lambda: self.validate(controller)).grid(row=9, column=0, columnspan=5)

        # Register Button
        tk.Label(self, text="").grid(row=10, column=0)    # Equivalent to empty line
        self.registerButton = tk.Button(self, text="Sign Up", height="1", width="15", command=lambda: controller.show_frame(Register)).grid(row=11, column=0, columnspan=2)

        # Back Button
        tk.Label(self, text="      ").grid(row=11, column=2)    # Equivalent to empty column
        self.backButton = tk.Button(self, text="Back", height="1", width="15", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=3, columnspan=2)
    

    # Reference: A Simple Login System With Python & Tkinter - https://medium.com/satyam-kulkarni/a-simple-login-system-with-python-tkinter-73e4c90820d7
    def validate(self, controller):      
        search = (self.username.get(),)
        inputData = (self.username.get(), self.password.get())

        if self.username.get() == "" or self.password.get() == "" or self.userType == "":
            messagebox.showerror("Required Fields", "Please input all required fields.")
            return

        try:
            if self.userType.get() == "Admin":
                if adminLoginDB.validate(search, inputData) == 1:    # Call function in Database Class
                    controller.show_frame(Dashboard)
                elif adminLoginDB.validate(search, inputData) == 0:
                    messagebox.showerror("Error", "User Does Not Exist!")
                else:
                    messagebox.showerror("Error", "Password Incorrect!")
            elif self.userType.get() == "Employee":
                if employeeLoginDB.validate(search, inputData) == 1:
                    controller.show_frame(Dashboard)
                elif employeeLoginDB.validate(search, inputData) == 0:
                    messagebox.showerror("Error", "User Does Not Exist!")
                else:
                    messagebox.showerror("Error", "Password Incorrect!")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")
        

# Register Window
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create register page element
        tk.Label(self, text="").grid(row=0, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        self.header = tk.Label(self, text="User Registration", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, columnspan=5)   # The first parameter: where to put the element

        self.userType = tk.StringVar()
        self.username = tk.StringVar()
        self.password1 = tk.StringVar()
        self.password2 = tk.StringVar()

        # Username Entry
        tk.Label(self, text="").grid(row=3, column=0)    # Equivalent to empty line
        self.usernameLabel = tk.Label(self, text="Enter Username: ", font=("Segoe UI", 11)).grid(row=4, column=0, sticky=tk.W, columnspan=3)
        self.usernameEntry = tk.Entry(self, textvariable=self.username)
        self.usernameEntry.grid(row=4, column=3, sticky=tk.W, columnspan=2)

        # Password Entry
        self.passwordLabel = tk.Label(self, text="Enter Password: ", font=("Segoe UI", 11)).grid(row=5, column=0, sticky=tk.W, columnspan=3)
        self.passwordEntry = tk.Entry(self, show="*", textvariable=self.password1)
        self.passwordEntry.grid(row=5, column=3, columnspan=2)
        
        # Password Re-Entry
        self.passwordLabel = tk.Label(self, text="Re-enter Password: ", font=("Segoe UI", 11)).grid(row=6, column=0, sticky=tk.W, columnspan=3)
        self.passwordEntry = tk.Entry(self, show="*", textvariable=self.password2)
        self.passwordEntry.grid(row=6, column=3, columnspan=2)

        # Role Selection
        tk.Label(self, text="").grid(row=7, column=0)    # Equivalent to empty line
        self.adminRadioButton = tk.Radiobutton(self, text="Administrator", variable=self.userType, value="Admin", font=("Segoe UI", 11)).grid(row=8, column=0, sticky=tk.W, columnspan=3)
        self.employeeRadioButton = tk.Radiobutton(self, text="Employee", variable=self.userType, value="Employee", font=("Segoe UI", 11)).grid(row=8, column=3, sticky=tk.E, columnspan=2)
        
        # Submit Button
        tk.Label(self, text="").grid(row=9, column=0, columnspan=2)    # Equivalent to empty line
        self.submitButton = tk.Button(self, text="Register", height="2", width="35", command=self.register).grid(row=10, column=0, columnspan=5)

        # Login Button
        tk.Label(self, text="").grid(row=11, column=0)    # Equivalent to empty line
        self.loginButton = tk.Button(self, text="Sign In", height="1", width="15", command=lambda: controller.show_frame(Login)).grid(row=12, column=0, columnspan=2)

        # Back Button
        tk.Label(self, text="      ").grid(row=12, column=2)    # Equivalent to empty column
        self.backButton = tk.Button(self, text="Back", height="1", width="15", command=lambda: controller.show_frame(Homepage)).grid(row=12, column=3, columnspan=2)


    def register(self):
        search = (self.username.get(),)
        inputData = (self.username.get(), self.password1.get())

        if self.username.get() == "" or self.password1.get() == "" or self.password2.get() == "" or self.userType == "":
            messagebox.showerror("Required Fields", "Please input all required fields.")
            return

        if self.password1.get() != self.password2.get():
            messagebox.showerror("Passwords Unmatched", "Please enter the same password in both password fields.")
            return

        try:
            if self.userType.get() == "Admin":
                if adminLoginDB.search(search) == 0:    # Call function in Database Class
                    adminLoginDB.insert(inputData)
                    messagebox.showinfo("Successful", "Register Successfully!")
                else:
                    messagebox.showwarning("Warning", "Username already Exists!")
            elif self.userType.get() == "Employee":
                if employeeLoginDB.search(search) == 0:
                    employeeLoginDB.insert(inputData)
                    messagebox.showinfo("Successful", "Register Successfully!")
                else:
                    messagebox.showwarning("Warning", "Username already Exists!")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")





# Start App
if __name__ == "__main__":
    app = App()
    app.run()



















    '''
    def create_widgets(self):
        # Create the homepage frame
        self.homepage_frame = Homepage(self)
        self.homepage_frame.pack()
    '''  

'''

# Create login window object
login = Tk()
login.title("Soundbox Dance Studios - Account Login")
login.iconbitmap("logo_ico.ico")
login.geometry("800x500")

# Create login page title label
knugenLogo = ImageTk.PhotoImage((Image.open("logo_png.png")))
logoLabel = Label(image=knugenLogo)
loginTitle = Label(login, text="Soundbox Dance Studios Login", font=("Segoe UI", 18, "bold"))         # The first parameter: where to put the element

userType = IntVar()

# userType.get()

adminRadioButton = Radiobutton(login, text="Admin", variable=userType, value=1, font=("Segoe UI", 12)).pack()
employeeRadioButton = Radiobutton(login, text="Employee", variable=userType, value=2, font=("Segoe UI", 12)).pack()

usernameLabel = Label(login, text="Username: ", font=("Segoe UI", 12))
# usernameInput = 
passwordLabel = Label(login, text="Password: ", font=("Segoe UI", 12))
# passwordInput = 

def loginAuth():
    if userType == 1:   # Admin login
        print("Admin Login!")

    if userType == 2:   # Employee login
        print("Employee Login!")


# loginButton = Button(login, text="Login", font=("Segoe UI", 12), command=login).pack()


# Display elements onto the screen
logoLabel.pack()
loginTitle.pack()
usernameLabel.pack()
passwordLabel.pack()

# Start program
login.mainloop()

'''
