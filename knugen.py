import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Account.employee_login_db import EmployeeLoginDB
from Account.admin_login_db import AdminLoginDB
from Course.course_db import CourseDB
from Membership.membership_status_db import MembershipStatusDB
from Membership.membership_type_db import MembershipTypeDB

# Reference: Tkinter Application to Switch Between Different Page Frames - https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# Database context
employeeLoginDB = EmployeeLoginDB()
adminLoginDB = AdminLoginDB()
courseDB = CourseDB()
membershipStatusDB = MembershipStatusDB()
membershipTypeDB = MembershipTypeDB()

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
        container.place(relx=0.5, rely=0.5, anchor="center")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing an empty frame array
        self.frames = {}

        for F in (Homepage, Login, Register, Dashboard, StudentDashboard, EmployeeDashboard, CourseDashboard, InventoryDashboard, MembershipDashboard, EventDashboard, AdminDashboard, 
                            Course, MembershipStatus, MembershipType): # CourseRecord
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
        self.header = tk.Label(self, text="User Login", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, columnspan=9)   # The first parameter: where to put the element

        self.userType = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Username Entry
        tk.Label(self, text="").grid(row=3, column=0)
        tk.Label(self, text="                                                                                               ").grid(row=4, column=0, columnspan=2)
        self.usernameLabel = tk.Label(self, text="Enter Username: ", font=("Segoe UI", 11)).grid(row=4, column=2, sticky=tk.W, columnspan=3)
        self.usernameEntry = tk.Entry(self, textvariable=self.username)
        self.usernameEntry.grid(row=4, column=5, sticky=tk.W, columnspan=2)
        tk.Label(self, text="                                                                                               ").grid(row=4, column=7, columnspan=2)

        # Password Entry
        self.passwordLabel = tk.Label(self, text="Enter Password: ", font=("Segoe UI", 11)).grid(row=5, column=2, sticky=tk.W, columnspan=3)
        self.passwordEntry = tk.Entry(self, show="*", textvariable=self.password)
        self.passwordEntry.grid(row=5, column=5, sticky=tk.W, columnspan=2)
        
        # Role Selection
        tk.Label(self, text="").grid(row=6, column=0)    # Equivalent to empty line
        self.adminRadioButton = tk.Radiobutton(self, text="Administrator", variable=self.userType, value="Admin", font=("Segoe UI", 11)).grid(row=7, column=2, sticky=tk.W, columnspan=3)
        self.employeeRadioButton = tk.Radiobutton(self, text="Employee", variable=self.userType, value="Employee", font=("Segoe UI", 11)).grid(row=7, column=5, sticky=tk.E, columnspan=2)
        
        # Submit Button
        tk.Label(self, text="").grid(row=8, column=0, columnspan=2)    # Equivalent to empty line
        self.submitButton = tk.Button(self, text="Login", height="2", width="35", command=lambda: self.validate(controller)).grid(row=9, column=2, columnspan=5)

        # Register Button
        tk.Label(self, text="").grid(row=10, column=0)    # Equivalent to empty line
        self.registerButton = tk.Button(self, text="Sign Up", height="1", width="15", command=lambda: controller.show_frame(Register)).grid(row=11, column=2, columnspan=2)

        # Back Button
        tk.Label(self, text="      ").grid(row=11, column=4)    # Equivalent to empty column
        self.backButton = tk.Button(self, text="Back", height="1", width="15", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=5, columnspan=2)
    

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
            
            # Clear the entry
            self.usernameEntry.delete(0, tk.END)
            self.passwordEntry.delete(0, tk.END)

        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")
        

# Register Window
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create register page element
        tk.Label(self, text="").grid(row=0, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        self.header = tk.Label(self, text="User Registration", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, columnspan=9)   # The first parameter: where to put the element

        self.userType = tk.StringVar()
        self.username = tk.StringVar()
        self.password1 = tk.StringVar()
        self.password2 = tk.StringVar()

        # Username Entry
        tk.Label(self, text="").grid(row=3, column=0)
        tk.Label(self, text="                                                                                               ").grid(row=4, column=0, columnspan=2)
        self.usernameLabel = tk.Label(self, text="Enter Username: ", font=("Segoe UI", 11)).grid(row=4, column=2, sticky=tk.W, columnspan=3)
        self.usernameEntry = tk.Entry(self, textvariable=self.username)
        self.usernameEntry.grid(row=4, column=5, sticky=tk.W, columnspan=2)
        tk.Label(self, text="                                                                                               ").grid(row=4, column=7, columnspan=2)

        # Password Entry
        self.passwordLabel1 = tk.Label(self, text="Enter Password: ", font=("Segoe UI", 11)).grid(row=5, column=2, sticky=tk.W, columnspan=3)
        self.passwordEntry1 = tk.Entry(self, show="*", textvariable=self.password1)
        self.passwordEntry1.grid(row=5, column=5, sticky=tk.W, columnspan=2)
        
        # Password Re-Entry
        self.passwordLabel2 = tk.Label(self, text="Re-enter Password: ", font=("Segoe UI", 11)).grid(row=6, column=2, sticky=tk.W, columnspan=3)
        self.passwordEntry2 = tk.Entry(self, show="*", textvariable=self.password2)
        self.passwordEntry2.grid(row=6, column=5, sticky=tk.W, columnspan=2)

        # Role Selection
        tk.Label(self, text="").grid(row=7, column=0)    # Equivalent to empty line
        self.adminRadioButton = tk.Radiobutton(self, text="Administrator", variable=self.userType, value="Admin", font=("Segoe UI", 11)).grid(row=8, column=2, sticky=tk.W, columnspan=3)
        self.employeeRadioButton = tk.Radiobutton(self, text="Employee", variable=self.userType, value="Employee", font=("Segoe UI", 11)).grid(row=8, column=5, sticky=tk.E, columnspan=2)
        
        # Submit Button
        tk.Label(self, text="").grid(row=9, column=0, columnspan=2)    # Equivalent to empty line
        self.submitButton = tk.Button(self, text="Register", height="2", width="35", command=self.register).grid(row=10, column=2, columnspan=5)

        # Login Button
        tk.Label(self, text="").grid(row=11, column=0)    # Equivalent to empty line
        self.loginButton = tk.Button(self, text="Sign In", height="1", width="15", command=lambda: controller.show_frame(Login)).grid(row=12, column=2, columnspan=2)

        # Back Button
        tk.Label(self, text="      ").grid(row=12, column=4)    # Equivalent to empty column
        self.backButton = tk.Button(self, text="Back", height="1", width="15", command=lambda: controller.show_frame(Homepage)).grid(row=12, column=5, columnspan=2)


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

            # Clear the entry
            self.usernameEntry.delete(0, tk.END)
            self.passwordEntry1.delete(0, tk.END)
            self.passwordEntry2.delete(0, tk.END)

        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")


# Dashboard Window
class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create dashboard page element
        self.header = tk.Label(self, text="Soundbox Studios Main Dashboard", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Student Button
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Button(self, text="Student", height="3", width="20", command=lambda: controller.show_frame(StudentDashboard)).grid(row=3, column=0)

        # 2. Employee Button
        tk.Label(self, text="      ").grid(row=3, column=1)    
        tk.Button(self, text="Employee", height="3", width="20", command=lambda: controller.show_frame(EmployeeDashboard)).grid(row=3, column=2)

        # 3. Course Button
        tk.Label(self, text="      ").grid(row=3, column=3)    
        tk.Button(self, text="Course", height="3", width="20", command=lambda: controller.show_frame(CourseDashboard)).grid(row=3, column=4)
        
        # 4. Inventory Button 
        tk.Label(self, text="      ").grid(row=3, column=5)    
        tk.Button(self, text="Inventory", height="3", width="20", command=lambda: controller.show_frame(InventoryDashboard)).grid(row=3, column=6)
        
        # 5. Membership Button
        tk.Label(self, text="      ").grid(row=3, column=7)    
        tk.Button(self, text="Membership", height="3", width="20", command=lambda: controller.show_frame(MembershipDashboard)).grid(row=3, column=8)
    
        # 6. Enrollment Button
        tk.Label(self, text="").grid(row=4, column=0)  
        tk.Label(self, text="").grid(row=5, column=0)  
        tk.Label(self, text="").grid(row=6, column=0)  
        tk.Label(self, text="").grid(row=7, column=0)  
        tk.Button(self, text="Enrollment", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=8, column=0)

        # 7. Reservation/Event Button
        tk.Label(self, text="      ").grid(row=8, column=1)    
        tk.Button(self, text="Reservation/Event", height="3", width="20", command=lambda: controller.show_frame(EventDashboard)).grid(row=8, column=2)

        # 8. Bill Button
        tk.Label(self, text="      ").grid(row=8, column=3)    
        tk.Button(self, text="Bill Record", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=8, column=4)

        # 9. Admin/Owner Button
        tk.Label(self, text="      ").grid(row=8, column=5)    
        tk.Button(self, text="Admin/Owner Information", height="3", width="20", command=lambda: controller.show_frame(AdminDashboard)).grid(row=8, column=6)

        # 10. Vendor Button
        tk.Label(self, text="      ").grid(row=8, column=7)    
        tk.Button(self, text="Vendor Information", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=8, column=8)

        # 11. Logout Button
        tk.Label(self, text="").grid(row=9, column=0)    
        tk.Label(self, text="").grid(row=10, column=0)    
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=8, sticky=tk.E)


# Student Sub-Dashboard Window
class StudentDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student dashboard page element
        self.header = tk.Label(self, text="Student Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Student Records
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Button(self, text="Student Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=0)

        # 2. Student Ratings/Reviews
        tk.Label(self, text="                    ").grid(row=3, column=1)    
        tk.Label(self, text="                    ").grid(row=3, column=2)    
        tk.Label(self, text="                    ").grid(row=3, column=3)    
        tk.Button(self, text="Student Ratings/Reviews", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=4)

        # 3. Student Contract List
        tk.Label(self, text="                    ").grid(row=3, column=5)    
        tk.Label(self, text="                    ").grid(row=3, column=6)    
        tk.Label(self, text="                    ").grid(row=3, column=7)    
        self.courseButton = tk.Button(self, text="Student Contract List", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=8)

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)  
        tk.Label(self, text="").grid(row=5, column=0)  
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=0, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=8, sticky=tk.E)


# Employee Sub-Dashboard Window
class EmployeeDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee dashboard page element
        self.header = tk.Label(self, text="Employee Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Employee Records
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Button(self, text="Employee Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=0)

        # 2. Employee Credentials
        tk.Label(self, text="                    ").grid(row=3, column=1)    
        tk.Label(self, text="                    ").grid(row=3, column=2)    
        tk.Label(self, text="                    ").grid(row=3, column=3)    
        tk.Button(self, text="Employee Credentials", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=4)

        # 3. Employee License Number
        tk.Label(self, text="                    ").grid(row=3, column=5)    
        tk.Label(self, text="                    ").grid(row=3, column=6)    
        tk.Label(self, text="                    ").grid(row=3, column=7)    
        self.courseButton = tk.Button(self, text="Employee License Number", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=8)

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)  
        tk.Label(self, text="").grid(row=5, column=0)  
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=0, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=8, sticky=tk.E)


# Course Sub-Dashboard Window
class CourseDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create course dashboard page element
        self.header = tk.Label(self, text="Course Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Course Records
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Course Records", height="8", width="20", command=lambda: controller.show_frame(Course)).grid(row=3, column=1)

        # 2. Student Course Status
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Student Course Status", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)


# Inventory Sub-Dashboard Window
class InventoryDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create inventory dashboard page element
        self.header = tk.Label(self, text="Inventory Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Merchandise Records
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Merchandise Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=1)

        # 2. Equipment Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Equipment Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)


# Membership Sub-Dashboard Window
class MembershipDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership dashboard page element
        self.header = tk.Label(self, text="Membership Infromation", font=("Segoe UI", 18, "bold")).pack()   # The first parameter: where to put the element

        # 1. Membership Records
        tk.Label(self, text="").pack()
        tk.Button(self, text="Membership", height="2", width="20", command=lambda: controller.show_frame(Homepage)).pack()

        # 2. Membership Status Records
        tk.Label(self, text="").pack()
        tk.Button(self, text="Membership Status", height="2", width="20", command=lambda: controller.show_frame(MembershipStatus)).pack()

        # 3. Membership Type Records
        tk.Label(self, text="").pack()
        tk.Button(self, text="Membership Type", height="2", width="20", command=lambda: controller.show_frame(MembershipType)).pack()

        # 4. Membership Number Records
        tk.Label(self, text="").pack()
        tk.Button(self, text="Membership Number", height="2", width="20", command=lambda: controller.show_frame(Homepage)).pack()

        # 4. Home Dashboard Button
        tk.Label(self, text="").pack()
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).pack()

        # 5. Logout Button
        tk.Label(self, text="").pack()
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).pack()


# Event Sub-Dashboard Window
class EventDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create event dashboard page element
        self.header = tk.Label(self, text="Reservations/Event Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Event Records
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Event Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=1)

        # 2. Reservation Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Reservation Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)


# Admin Sub-Dashboard Window
class AdminDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create admin dashboard page element
        self.header = tk.Label(self, text="Admin/Owner Infromation", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Admin Records/Credentials
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Admin Records/Credentials", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=1)

        # 2. Owner Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Owner Records", height="8", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)


# Course Window
class Course(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create course page element
        self.header = tk.Label(self, text="Course Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)

        # Store selected item
        self.selected_item = 0
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):
        # Employee ID
        self.employeeid_text = tk.StringVar()
        self.employeeid_label = tk.Label(self, text='Employee ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.employeeid_entry = tk.Entry(self, textvariable=self.employeeid_text)
        self.employeeid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Genre ID
        self.genreid_text = tk.StringVar()
        self.genreid_label = tk.Label(self, text='Genre ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.genreid_entry = tk.Entry(self, textvariable=self.genreid_text)
        self.genreid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Course Price ID
        self.coursepriceid_text = tk.StringVar()
        self.coursepriceid_label = tk.Label(self, text='Course Price ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.coursepriceid_entry = tk.Entry(self, textvariable=self.coursepriceid_text)
        self.coursepriceid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Course Number ID
        self.coursenumberid_text = tk.StringVar()
        self.coursenumberid_label = tk.Label(self, text='Course Number ID: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.coursenumberid_entry = tk.Entry(self, textvariable=self.coursenumberid_text)
        self.coursenumberid_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Course Name
        self.course_name_text = tk.StringVar()
        self.course_name_label = tk.Label(self, text='Course Name: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.course_name_entry = tk.Entry(self, textvariable=self.course_name_text)
        self.course_name_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

        # Course Date
        self.course_date_text = tk.StringVar()
        self.course_date_label = tk.Label(self, text='Course Date: ', font=("Segoe UI", 11)).grid(row=4, column=0, sticky=tk.W)
        self.course_date_entry = tk.Entry(self, textvariable=self.course_date_text)
        self.course_date_entry.grid(row=4, column=1)
        tk.Label(self, text="          ").grid(row=4, column=2)

        # Course Time
        self.course_time_text = tk.StringVar()
        self.course_time_label = tk.Label(self, text='Course Time: ', font=("Segoe UI", 11)).grid(row=4, column=3, sticky=tk.W)
        self.course_time_entry = tk.Entry(self, textvariable=self.course_time_text)
        self.course_time_entry.grid(row=4, column=4)
        tk.Label(self, text="          ").grid(row=4, column=5)

        # Buttons
        tk.Label(self, text="").grid(row=5, column=0)
        self.add_btn = tk.Button(self, text="Add Record", font=("Segoe UI", 10), width=14, command=self.add_item)
        self.add_btn.grid(row=6, column=0, sticky=tk.E)  

        self.update_btn = tk.Button(self, text="Update Record", font=("Segoe UI", 10), width=14, command=self.update_item)
        self.update_btn.grid(row=6, column=1, sticky=tk.E)

        self.remove_btn = tk.Button(self, text="Remove Record", font=("Segoe UI", 10), width=14, command=self.remove_item)
        self.remove_btn.grid(row=6, column=3, sticky=tk.E)

        self.exit_btn = tk.Button(self, text="Clear Input", font=("Segoe UI", 10), width=14, command=self.clear_text)
        self.exit_btn.grid(row=6, column=4, sticky=tk.E)

        # Course List
        tk.Label(self, text="").grid(row=7, column=0)
        self.courses_list = tk.Listbox(self, height=7, width=130, border=1)
        self.courses_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(CourseDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.courses_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.courses_list.yview)

        # Bind select
        self.courses_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.courses_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.courses_list.get(index)

            # Display data at entry box
            self.employeeid_entry.delete(0, tk.END)
            self.employeeid_entry.insert(tk.END, self.selected_item[1])
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[2])
            self.genreid_entry.delete(0, tk.END)
            self.genreid_entry.insert(tk.END, self.selected_item[3])
            self.coursepriceid_entry.delete(0, tk.END)
            self.coursepriceid_entry.insert(tk.END, self.selected_item[4])
            self.coursenumberid_entry.delete(0, tk.END)
            self.coursenumberid_entry.insert(tk.END, self.selected_item[5])
            self.course_name_entry.delete(0, tk.END)
            self.course_name_entry.insert(tk.END, self.selected_item[6])
            self.course_date_entry.delete(0, tk.END)
            self.course_date_entry.insert(tk.END, self.selected_item[7])
            self.course_time_entry.delete(0, tk.END)
            self.course_time_entry.insert(tk.END, self.selected_item[8])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.employeeid_text.get() == '' or self.studentid_text.get() == '' or self.genreid_text.get() == '' \
                                            or self.coursepriceid_text.get() == '' or self.coursenumberid_text.get() == '' \
                                            or self.course_name_text.get() == '' or self.course_date_text.get() == '' \
                                            or self.course_time_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        courseDB.insert(self.employeeid_text.get(), self.studentid_text.get(), self.genreid_text.get(),
                        self.coursepriceid_text.get(), self.coursenumberid_text.get(), self.course_name_text.get(),
                        self.course_date_text.get(), self.course_time_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        courseDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        courseDB.update(self.selected_item[0], self.employeeid_text.get(), self.studentid_text.get(), self.genreid_text.get(),
                        self.coursepriceid_text.get(), self.coursenumberid_text.get(), self.course_name_text.get(),
                        self.course_date_text.get(), self.course_time_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.employeeid_entry.delete(0, tk.END)
        self.studentid_entry.delete(0, tk.END)
        self.genreid_entry.delete(0, tk.END)
        self.coursepriceid_entry.delete(0, tk.END)
        self.coursenumberid_entry.delete(0, tk.END)
        self.course_name_entry.delete(0, tk.END)
        self.course_date_entry.delete(0, tk.END)
        self.course_time_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.courses_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in courseDB.fetch():
            line = [row.courseid, row.employeeid, row.studentid, row.genreid, row.coursepriceid, row.coursenumberid, row.course_name,
                    row.course_date, row.course_time]
            self.courses_list.insert(tk.END, line)
        

# Membership Status Window
class MembershipStatus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership status page element
        self.header = tk.Label(self, text="Membership Status Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Membership Status List
        tk.Label(self, text="").grid(row=7, column=0)
        self.membership_status_list = tk.Listbox(self, height=7, width=130, border=1)
        self.membership_status_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(MembershipDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.membership_status_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.membership_status_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.membership_status_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in membershipStatusDB.fetch():
            line = [row.membershipstatusid, row.membership_status]
            self.membership_status_list.insert(tk.END, line)


# Membership Type Window
class MembershipType(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership type page element
        self.header = tk.Label(self, text="Membership Type Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Membership Type List
        tk.Label(self, text="").grid(row=7, column=0)
        self.membership_type_list = tk.Listbox(self, height=7, width=130, border=1)
        self.membership_type_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(MembershipDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.membership_type_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.membership_type_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.membership_type_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in membershipTypeDB.fetch():
            line = [row.membershiptypeid, row.membership_type]
            self.membership_type_list.insert(tk.END, line)




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
