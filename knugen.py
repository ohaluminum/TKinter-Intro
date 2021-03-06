import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Student.student_db import StudentDB
from Student.student_record_db import StudentRecordDB
from Student.student_rating_db import StudentRatingDB
from Student.student_review_db import StudentReviewDB
from Student.student_rating_record_db import StudentRatingRecordDB
from Student.student_contract_db import StudentContractDB
from Student.student_contract_record_db import StudentContractRecordDB
from Employee.employee_db import EmployeeDB
from Employee.employee_record_db import EmployeeRecordDB
from Employee.employee_credential_db import EmployeeCredentialDB
from Employee.employee_credential_record_db import EmployeeCredentialRecordDB
from Employee.employee_login_db import EmployeeLoginDB
from Employee.employee_license_db import EmployeeLicenseDB
from Employee.employee_license_number_db import EmployeeLicenseNumberDB
from Employee.employee_license_record_db import EmployeeLicenseRecordDB
from Course.course_db import CourseDB
from Course.course_record_db import CourseRecordDB
from Course.student_course_status_db import StudentCourseStatusDB
from Course.student_course_status_record_db import StudentCourseStatusRecordDB
from Membership.membership_db import MembershipDB
from Membership.membership_record_db import MembershipRecordDB
from Enrollment.enrollment_db import EnrollmentDB
from Enrollment.enrollment_record_db import EnrollmentRecordDB
from Merchandise.merchandise_db import MerchandiseDB
from Merchandise.merchandise_record_db import MerchandiseRecordDB
from Equipment.equipment_db import EquipmentDB
from Equipment.equipment_record_db import EquipmentRecordDB
from Event.event_db import EventDB
from Event.event_status_db import EventStatusDB
from Event.event_record_db import EventRecordDB
from Event.dance_team_db import DanceTeamDB
from Event.reservation_db import ReservationDB
from Event.reservation_record_db import ReservationRecordDB
from Bill.bill_db import BillDB
from Bill.bill_record_db import BillRecordDB
from Admin.admin_db import AdminDB
from Admin.admin_info_db import AdminInfoDB
from Admin.admin_login_db import AdminLoginDB
from Admin.admin_record_db import AdminRecordDB
from Admin.owner_db import OwnerDB
from Admin.owner_record_db import OwnerRecordDB
from Vendor.vendor_db import VendorDB
from Vendor.vendor_record_db import VendorRecordDB

# Reference: Tkinter Application to Switch Between Different Page Frames - https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

# Database context
studentDB = StudentDB()
studentRecordDB = StudentRecordDB()
studentRatingDB = StudentRatingDB()
studentReviewDB = StudentReviewDB()
studentRatingRecordDB = StudentRatingRecordDB()
studentContractDB = StudentContractDB()
studentContractRecordDB = StudentContractRecordDB()
employeeDB = EmployeeDB()
employeeRecordDB = EmployeeRecordDB()
employeeCredentialDB = EmployeeCredentialDB()
employeeCredentialRecordDB = EmployeeCredentialRecordDB()
employeeLoginDB = EmployeeLoginDB()
employeeLicenseDB = EmployeeLicenseDB()
employeeLicenseNumberDB = EmployeeLicenseNumberDB()
employeeLicenseRecordDB = EmployeeLicenseRecordDB()
courseDB = CourseDB()
courseRecordDB = CourseRecordDB()
studentCourseStatusDB = StudentCourseStatusDB()
studentCourseStatusRecordDB = StudentCourseStatusRecordDB()
merchandiseDB = MerchandiseDB()
merchandiseRecordDB = MerchandiseRecordDB()
equipmentDB = EquipmentDB()
equipmentRecordDB = EquipmentRecordDB()
membershipDB = MembershipDB()
membershipRecordDB = MembershipRecordDB()
enrollmentDB = EnrollmentDB()
enrollmentRecordDB = EnrollmentRecordDB()
eventDB = EventDB()
eventStatusDB = EventStatusDB()
eventRecordDB = EventRecordDB()
danceTeamDB = DanceTeamDB()
reservationDB = ReservationDB()
reservationRecordDB = ReservationRecordDB()
billDB = BillDB()
billRecordDB = BillRecordDB()
adminDB = AdminDB()
adminInfoDB = AdminInfoDB()
adminLoginDB = AdminLoginDB()
adminRecordDB = AdminRecordDB()
ownerDB = OwnerDB()
ownerRecordDB = OwnerRecordDB()
vendorDB = VendorDB()
vendorRecordDB = VendorRecordDB()


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

        for F in (Homepage, Login, Register, Dashboard, StudentDashboard, EmployeeDashboard, CourseDashboard, InventoryDashboard, EventDashboard, AdminDashboard,
                        StudentRecord, Student, StudentRatingRecord, StudentRating, StudentReview, StudentContractRecord, StudentContract,
                        EmployeeRecord, Employee, EmployeeCredentialRecord, EmployeeCredential, EmployeeLogin, EmployeeLicenseRecord, EmployeeLicense, EmployeeLicenseNumber,
                        CourseRecord, Course, StudentCourseStatusRecord, StudentCourseStatus, MerchandiseRecord, Merchandise, EquipmentRecord, Equipment, MembershipRecord, Membership, EnrollmentRecord, Enrollment,
                        EventRecord, Event, EventStatus, DanceTeam, ReservationRecord, Reservation, BillRecord, Bill, AdminRecord, Admin, AdminInfo, AdminLogin, OwnerRecord, Owner, VendorRecord, Vendor):
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
        tk.Label(self, text="").grid(row=1, column=0)
        tk.Label(self, text="").grid(row=2, column=0)
        tk.Button(self, text="Student", height="3", width="20", command=lambda: controller.show_frame(StudentDashboard)).grid(row=3, column=0)      # ???

        # 2. Employee Button
        tk.Label(self, text="      ").grid(row=3, column=1)    
        tk.Button(self, text="Employee", height="3", width="20", command=lambda: controller.show_frame(EmployeeDashboard)).grid(row=3, column=2)        # ???

        # 3. Course Button
        tk.Label(self, text="      ").grid(row=3, column=3)    
        tk.Button(self, text="Course", height="3", width="20", command=lambda: controller.show_frame(CourseDashboard)).grid(row=3, column=4)
        
        # 4. Inventory Button 
        tk.Label(self, text="      ").grid(row=3, column=5)    
        tk.Button(self, text="Inventory", height="3", width="20", command=lambda: controller.show_frame(InventoryDashboard)).grid(row=3, column=6)       # ???
        
        # 5. Membership Button
        tk.Label(self, text="      ").grid(row=3, column=7)    
        tk.Button(self, text="Membership", height="3", width="20", command=lambda: controller.show_frame(MembershipRecord)).grid(row=3, column=8)        # ???
    
        # 6. Enrollment Button
        tk.Label(self, text="").grid(row=4, column=0)  
        tk.Label(self, text="").grid(row=5, column=0)  
        tk.Label(self, text="").grid(row=6, column=0)  
        tk.Label(self, text="").grid(row=7, column=0)  
        tk.Button(self, text="Enrollment", height="3", width="20", command=lambda: controller.show_frame(EnrollmentRecord)).grid(row=8, column=0)       # ???

        # 7. Reservation/Event Button
        tk.Label(self, text="      ").grid(row=8, column=1)    
        tk.Button(self, text="Reservation/Event", height="3", width="20", command=lambda: controller.show_frame(EventDashboard)).grid(row=8, column=2)      # ???

        # 8. Bill Button
        tk.Label(self, text="      ").grid(row=8, column=3)    
        tk.Button(self, text="Bill", height="3", width="20", command=lambda: controller.show_frame(BillRecord)).grid(row=8, column=4)       # ???

        # 9. Admin/Owner Button
        tk.Label(self, text="      ").grid(row=8, column=5)    
        tk.Button(self, text="Admin/Owner", height="3", width="20", command=lambda: controller.show_frame(AdminDashboard)).grid(row=8, column=6)        # ???

        # 10. Vendor Button
        tk.Label(self, text="      ").grid(row=8, column=7)    
        tk.Button(self, text="Vendor", height="3", width="20", command=lambda: controller.show_frame(VendorRecord)).grid(row=8, column=8)       # ???

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
        tk.Button(self, text="Student Records", height="8", width="20", command=lambda: controller.show_frame(StudentRecord)).grid(row=3, column=0)

        # 2. Student Ratings/Reviews
        tk.Label(self, text="                    ").grid(row=3, column=1)    
        tk.Label(self, text="                    ").grid(row=3, column=2)    
        tk.Label(self, text="                    ").grid(row=3, column=3)    
        tk.Button(self, text="Student Ratings/Reviews", height="8", width="20", command=lambda: controller.show_frame(StudentRatingRecord)).grid(row=3, column=4)

        # 3. Student Contract List
        tk.Label(self, text="                    ").grid(row=3, column=5)    
        tk.Label(self, text="                    ").grid(row=3, column=6)    
        tk.Label(self, text="                    ").grid(row=3, column=7)    
        self.courseButton = tk.Button(self, text="Student Contract", height="8", width="20", command=lambda: controller.show_frame(StudentContractRecord)).grid(row=3, column=8)

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
        tk.Button(self, text="Employee Records", height="8", width="20", command=lambda: controller.show_frame(EmployeeRecord)).grid(row=3, column=0)

        # 2. Employee Credentials
        tk.Label(self, text="                    ").grid(row=3, column=1)    
        tk.Label(self, text="                    ").grid(row=3, column=2)    
        tk.Label(self, text="                    ").grid(row=3, column=3)    
        tk.Button(self, text="Employee Credentials", height="8", width="20", command=lambda: controller.show_frame(EmployeeCredentialRecord)).grid(row=3, column=4)

        # 3. Employee License Number
        tk.Label(self, text="                    ").grid(row=3, column=5)    
        tk.Label(self, text="                    ").grid(row=3, column=6)    
        tk.Label(self, text="                    ").grid(row=3, column=7)    
        self.courseButton = tk.Button(self, text="Employee License Number", height="8", width="20", command=lambda: controller.show_frame(EmployeeLicenseRecord)).grid(row=3, column=8)

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
        tk.Button(self, text="Course Records", height="8", width="20", command=lambda: controller.show_frame(CourseRecord)).grid(row=3, column=1)

        # 2. Student Course Status
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Student Course Status", height="8", width="20", command=lambda: controller.show_frame(StudentCourseStatusRecord)).grid(row=3, column=7)
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
        tk.Label(self, text="").grid(row=1, column=0)
        tk.Label(self, text="").grid(row=2, column=0)
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Merchandise Records", height="8", width="20", command=lambda: controller.show_frame(MerchandiseRecord)).grid(row=3, column=1)

        # 2. Equipment Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Equipment Records", height="8", width="20", command=lambda: controller.show_frame(EquipmentRecord)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)


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
        tk.Button(self, text="Event Records", height="8", width="20", command=lambda: controller.show_frame(EventRecord)).grid(row=3, column=1)

        # 2. Reservation Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Reservation Records", height="8", width="20", command=lambda: controller.show_frame(ReservationRecord)).grid(row=3, column=7)
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
        self.header = tk.Label(self, text="Admin/Owner Information", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element

        # 1. Admin Records/Credentials
        tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=2, column=0)    # Equivalent to empty line
        tk.Label(self, text="                                                     ").grid(row=3, column=0)
        tk.Button(self, text="Admin Records", height="8", width="20", command=lambda: controller.show_frame(AdminRecord)).grid(row=3, column=1)

        # 2. Owner Records
        tk.Label(self, text="                                                                   ").grid(row=3, column=2, columnspan=5)    
        tk.Button(self, text="Owner Records", height="8", width="20", command=lambda: controller.show_frame(OwnerRecord)).grid(row=3, column=7)
        tk.Label(self, text="                                                     ").grid(row=3, column=8)    

        # 4. Home Dashboard Button
        tk.Label(self, text="").grid(row=4, column=0)
        tk.Label(self, text="").grid(row=5, column=0)
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=6, column=1, sticky=tk.W)

        # 5. Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=6, column=7, sticky=tk.E)

# ------------------------------------------- STUDENT ------------------------------------------------ 

# Student Record Window
class StudentRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student record page element
        self.header = tk.Label(self, text="Student Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Student Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_list = tk.Listbox(self, height=15, width=130, border=1)
        self.student_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Student)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentRecordDB.fetch():
            self.student_list.insert(tk.END, row)


# Student Window
class Student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student page element
        self.header = tk.Label(self, text="Student Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Address ID
        self.addressid_text = tk.StringVar()
        self.addressid_label = tk.Label(self, text='Address ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.addressid_entry = tk.Entry(self, textvariable=self.addressid_text)
        self.addressid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # First Name
        self.first_name_text = tk.StringVar()
        self.first_name_label = tk.Label(self, text='First Name: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Last Name
        self.last_name_text = tk.StringVar()
        self.last_name_label = tk.Label(self, text='Last Name: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Phone
        self.phone_text = tk.StringVar()
        self.phone_label = tk.Label(self, text='Phone: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self, textvariable=self.phone_text)
        self.phone_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Email
        self.email_text = tk.StringVar()
        self.email_label = tk.Label(self, text='Email: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.email_entry = tk.Entry(self, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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

        # Student List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_list = tk.Listbox(self, height=7, width=130, border=1)
        self.student_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_list.yview)

        # Bind select
        self.student_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.student_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.student_list.get(index)

            # Display data at entry box
            self.addressid_entry.delete(0, tk.END)
            self.addressid_entry.insert(tk.END, self.selected_item[1])
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(tk.END, self.selected_item[2])
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(tk.END, self.selected_item[3])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, self.selected_item[4])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.addressid_text.get() == '' or self.first_name_text.get() == '' or self.last_name_text.get() == '' \
                                            or self.phone_text.get() == '' or self.email_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        studentDB.insert(self.addressid_text.get(), self.first_name_text.get(), self.last_name_text.get(), 
                        self.phone_text.get(), self.email_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        studentDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        studentDB.update(self.selected_item[0], self.addressid_text.get(), self.first_name_text.get(),
                        self.last_name_text.get(), self.phone_text.get(), self.email_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.addressid_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.student_list.insert(tk.END, line)


# Student Rating Record Window
class StudentRatingRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student rating record page element
        self.header = tk.Label(self, text="Student Rating Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Student Rating Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_rating_list = tk.Listbox(self, height=15, width=130, border=1)
        self.student_rating_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit Rating", height="1", width="15", command=lambda: controller.show_frame(StudentRating)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Review", height="1", width="15", command=lambda: controller.show_frame(StudentReview)).grid(row=11, column=3, sticky=tk.W)
        tk.Button(self, text="Edit Student", height="1", width="15", command=lambda: controller.show_frame(Student)).grid(row=11, column=4, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_rating_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_rating_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_rating_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentRatingRecordDB.fetch():
            self.student_rating_list.insert(tk.END, row)


# Student Rating Window
class StudentRating(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student rating page element
        self.header = tk.Label(self, text="Student Rating Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Student Category ID
        self.studentcategoryid_text = tk.StringVar()
        self.studentcategoryid_label = tk.Label(self, text='Category ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.studentcategoryid_entry = tk.Entry(self, textvariable=self.studentcategoryid_text)
        self.studentcategoryid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Course ID
        self.courseid_text = tk.StringVar()
        self.courseid_label = tk.Label(self, text='Course ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.courseid_entry = tk.Entry(self, textvariable=self.courseid_text)
        self.courseid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Student Review ID
        self.studentreviewid_text = tk.StringVar()
        self.studentreviewid_label = tk.Label(self, text='Review ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.studentreviewid_entry = tk.Entry(self, textvariable=self.studentreviewid_text)
        self.studentreviewid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Rating Number
        self.rating_number_text = tk.StringVar()
        self.rating_number_label = tk.Label(self, text='Rating Number: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.rating_number_entry = tk.Entry(self, textvariable=self.rating_number_text)
        self.rating_number_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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

        # Student List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_rating_list = tk.Listbox(self, height=7, width=130, border=1)
        self.student_rating_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentRatingRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_rating_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_rating_list.yview)

        # Bind select
        self.student_rating_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.student_rating_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.student_rating_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.studentcategoryid_entry.delete(0, tk.END)
            self.studentcategoryid_entry.insert(tk.END, self.selected_item[2])
            self.courseid_entry.delete(0, tk.END)
            self.courseid_entry.insert(tk.END, self.selected_item[3])
            self.studentreviewid_entry.delete(0, tk.END)
            self.studentreviewid_entry.insert(tk.END, self.selected_item[4])
            self.rating_number_entry.delete(0, tk.END)
            self.rating_number_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.studentcategoryid_text.get() == '' or self.courseid_text.get() == '' \
                                            or self.studentreviewid_text.get() == '' or self.rating_number_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        studentRatingDB.insert(self.studentid_text.get(), self.studentcategoryid_text.get(), self.courseid_text.get(), 
                            self.studentreviewid_text.get(), self.rating_number_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        studentRatingDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        studentRatingDB.update(self.selected_item[0], self.studentid_text.get(), self.studentcategoryid_text.get(), self.courseid_text.get(),
                            self.studentreviewid_text.get(), self.rating_number_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.studentcategoryid_entry.delete(0, tk.END)
        self.courseid_entry.delete(0, tk.END)
        self.studentreviewid_entry.delete(0, tk.END)
        self.rating_number_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_rating_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentRatingDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.student_rating_list.insert(tk.END, line)


# Student Review Window
class StudentReview(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student review page element
        self.header = tk.Label(self, text="Student Review Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student Review Comment
        self.student_review_comment_text = tk.StringVar()
        self.student_review_comment_label = tk.Label(self, text='Review Comment: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.student_review_comment_entry = tk.Entry(self, textvariable=self.student_review_comment_text)
        self.student_review_comment_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Student Review Date
        self.student_review_date_text = tk.StringVar()
        self.student_review_date_label = tk.Label(self, text='Review Date: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.student_review_date_entry = tk.Entry(self, textvariable=self.student_review_date_text)
        self.student_review_date_entry.grid(row=2, column=4)
        tk.Label(self, text="                                                                                                              ").grid(row=2, column=5, columnspan=4)

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

        # Riview List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_review_list = tk.Listbox(self, height=7, width=130, border=1)
        self.student_review_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentRatingRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_review_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_review_list.yview)

        # Bind select
        self.student_review_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.student_review_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.student_review_list.get(index)

            # Display data at entry box
            self.student_review_comment_entry.delete(0, tk.END)
            self.student_review_comment_entry.insert(tk.END, self.selected_item[1])
            self.student_review_date_entry.delete(0, tk.END)
            self.student_review_date_entry.insert(tk.END, self.selected_item[2])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.student_review_comment_text.get() == '' or self.student_review_date_text.get() == '':           
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        studentReviewDB.insert(self.student_review_comment_text.get(), self.student_review_date_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        studentReviewDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        studentReviewDB.update(self.selected_item[0], self.student_review_comment_text.get(), self.student_review_date_text.get())
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.student_review_comment_entry.delete(0, tk.END)
        self.student_review_date_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_review_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentReviewDB.fetch():
            line = [row[0], row[1], row[2]]
            self.student_review_list.insert(tk.END, line)


# Student Contract Record Window
class StudentContractRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student contract record page element
        self.header = tk.Label(self, text="Student Contract Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Student Rating Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_contract_list = tk.Listbox(self, height=15, width=130, border=1)
        self.student_contract_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit Contract", height="1", width="15", command=lambda: controller.show_frame(StudentContract)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Student", height="1", width="15", command=lambda: controller.show_frame(Student)).grid(row=11, column=3, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_contract_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_contract_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_contract_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentContractRecordDB.fetch():
            self.student_contract_list.insert(tk.END, row)


# Student Contract Window
class StudentContract(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student contract page element
        self.header = tk.Label(self, text="Student Contract Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Student Category ID
        self.studentcategoryid_text = tk.StringVar()
        self.studentcategoryid_label = tk.Label(self, text='Category ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.studentcategoryid_entry = tk.Entry(self, textvariable=self.studentcategoryid_text)
        self.studentcategoryid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Student Code ID
        self.studentcodeid_text = tk.StringVar()
        self.studentcodeid_label = tk.Label(self, text='Student Code ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.studentcodeid_entry = tk.Entry(self, textvariable=self.studentcodeid_text)
        self.studentcodeid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Student Contract Status ID
        self.studentcontractstatusid_text = tk.StringVar()
        self.studentcontractstatusid_label = tk.Label(self, text='Contract Status ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.studentcontractstatusid_entry = tk.Entry(self, textvariable=self.studentcontractstatusid_text)
        self.studentcontractstatusid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

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

        # Student List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_contract_list = tk.Listbox(self, height=7, width=130, border=1)
        self.student_contract_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentContractRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_contract_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_contract_list.yview)

        # Bind select
        self.student_contract_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.student_contract_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.student_contract_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.studentcategoryid_entry.delete(0, tk.END)
            self.studentcategoryid_entry.insert(tk.END, self.selected_item[2])
            self.studentcodeid_entry.delete(0, tk.END)
            self.studentcodeid_entry.insert(tk.END, self.selected_item[3])
            self.studentcontractstatusid_entry.delete(0, tk.END)
            self.studentcontractstatusid_entry.insert(tk.END, self.selected_item[4])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.studentcategoryid_text.get() == '' or self.studentcodeid_text.get() == '' \
                                            or self.studentcontractstatusid_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        studentContractDB.insert(self.studentid_text.get(), self.studentcategoryid_text.get(), self.studentcodeid_text.get(),
                                self.studentcontractstatusid_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        studentContractDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        studentContractDB.update(self.selected_item[0], self.studentid_text.get(), self.studentcategoryid_text.get(), self.studentcodeid_text.get(),
                                self.studentcontractstatusid_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.studentcategoryid_entry.delete(0, tk.END)
        self.studentcodeid_entry.delete(0, tk.END)
        self.studentcontractstatusid_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_contract_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentContractDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4]]
            self.student_contract_list.insert(tk.END, line)


# ------------------------------------------- Employee ------------------------------------------------ 

# Employee Record Window
class EmployeeRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee record page element
        self.header = tk.Label(self, text="Employee Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Employee Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_list = tk.Listbox(self, height=15, width=130, border=1)
        self.employee_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="15", command=lambda: controller.show_frame(Employee)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeRecordDB.fetch():
            self.employee_list.insert(tk.END, row)


# Employee Window   
class Employee(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee page element
        self.header = tk.Label(self, text="Employee Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Address ID
        self.addressid_text = tk.StringVar()
        self.addressid_label = tk.Label(self, text='Address ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.addressid_entry = tk.Entry(self, textvariable=self.addressid_text)
        self.addressid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # First Name
        self.first_name_text = tk.StringVar()
        self.first_name_label = tk.Label(self, text='First Name: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Last Name
        self.last_name_text = tk.StringVar()
        self.last_name_label = tk.Label(self, text='Last Name: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Phone
        self.phone_text = tk.StringVar()
        self.phone_label = tk.Label(self, text='Phone: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self, textvariable=self.phone_text)
        self.phone_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Email
        self.email_text = tk.StringVar()
        self.email_label = tk.Label(self, text='Email: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.email_entry = tk.Entry(self, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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

        # Employee List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_list = tk.Listbox(self, height=7, width=130, border=1)
        self.employee_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_list.yview)

        # Bind select
        self.employee_list.bind('<<ListboxSelect>>', self.select_item)


    def select_item(self, event):
        try:
            # Get index
            index = self.employee_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.employee_list.get(index)

            # Display data at entry box
            self.addressid_entry.delete(0, tk.END)
            self.addressid_entry.insert(tk.END, self.selected_item[1])
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(tk.END, self.selected_item[2])
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(tk.END, self.selected_item[3])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, self.selected_item[4])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.addressid_text.get() == '' or self.first_name_text.get() == '' or self.last_name_text.get() == '' \
                                            or self.phone_text.get() == '' or self.email_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        employeeDB.insert(self.addressid_text.get(), self.first_name_text.get(), self.last_name_text.get(), 
                        self.phone_text.get(), self.email_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        employeeDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        employeeDB.update(self.selected_item[0], self.addressid_text.get(), self.first_name_text.get(),
                        self.last_name_text.get(), self.phone_text.get(), self.email_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.addressid_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.employee_list.insert(tk.END, line)


# Employee Credential Record Window
class EmployeeCredentialRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee credential record page element
        self.header = tk.Label(self, text="Employee Credential Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Employee Credential Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_credential_list = tk.Listbox(self, height=15, width=130, border=1)
        self.employee_credential_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit Credential", height="1", width="15", command=lambda: controller.show_frame(EmployeeCredential)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Login", height="1", width="15", command=lambda: controller.show_frame(EmployeeLogin)).grid(row=11, column=3, sticky=tk.W)
        tk.Button(self, text="Edit Employee", height="1", width="15", command=lambda: controller.show_frame(Employee)).grid(row=11, column=4, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_credential_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_credential_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_credential_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeCredentialRecordDB.fetch():
            self.employee_credential_list.insert(tk.END, row)


# Employee Credential Window
class EmployeeCredential(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee page element
        self.header = tk.Label(self, text="Employee Credential Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Employee ID
        self.employeeid_text = tk.StringVar()
        self.employeeid_label = tk.Label(self, text='Employee ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.employeeid_entry = tk.Entry(self, textvariable=self.employeeid_text)
        self.employeeid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Employee Type
        self.employeetypeid_text = tk.StringVar()
        self.employeetypeid_label = tk.Label(self, text='Type ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.employeetypeid_entry = tk.Entry(self, textvariable=self.employeetypeid_text)
        self.employeetypeid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Employee Status
        self.employeestatusid_text = tk.StringVar()
        self.employeestatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.employeestatusid_entry = tk.Entry(self, textvariable=self.employeestatusid_text)
        self.employeestatusid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Employee Login
        self.employeeloginid_text = tk.StringVar()
        self.employeeloginid_label = tk.Label(self, text='Login ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.employeeloginid_entry = tk.Entry(self, textvariable=self.employeeloginid_text)
        self.employeeloginid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

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

        # Employee Credential List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_credential_list = tk.Listbox(self, height=7, width=130, border=1)
        self.employee_credential_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeCredentialRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_credential_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_credential_list.yview)

        # Bind select
        self.employee_credential_list.bind('<<ListboxSelect>>', self.select_item)

        

    def select_item(self, event):
        try:
            # Get index
            index = self.employee_credential_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.employee_credential_list.get(index)

            # Display data at entry box
            self.employeeid_entry.delete(0, tk.END)
            self.employeeid_entry.insert(tk.END, self.selected_item[1])
            self.employeetypeid_entry.delete(0, tk.END)
            self.employeetypeid_entry.insert(tk.END, self.selected_item[2])
            self.employeestatusid_entry.delete(0, tk.END)
            self.employeestatusid_entry.insert(tk.END, self.selected_item[3])
            self.employeeloginid_entry.delete(0, tk.END)
            self.employeeloginid_entry.insert(tk.END, self.selected_item[4])


        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.employeeid_text.get() == '' or self.employeetypeid_text.get() == '' or self.employeestatusid_text.get() == '' \
                                            or self.employeeloginid_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        employeeCredentialDB.insert(self.employeeid_text.get(), self.employeetypeid_text.get(), self.employeestatusid_text.get(), 
                        self.employeeloginid_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        employeeCredentialDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        employeeCredentialDB.update(self.selected_item[0], self.employeeid_text.get(), self.employeetypeid_text.get(), self.employeestatusid_text.get(), 
                        self.employeeloginid_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.employeeid_entry.delete(0, tk.END)
        self.employeetypeid_entry.delete(0, tk.END)
        self.employeestatusid_entry.delete(0, tk.END)
        self.employeeloginid_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_credential_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeCredentialDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4]]
            self.employee_credential_list.insert(tk.END, line)


# Employee Login Window
class EmployeeLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee login page element
        self.header = tk.Label(self, text="Employee Login Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Employee Username
        self.employee_username_text = tk.StringVar()
        self.employee_username_label = tk.Label(self, text='Username: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.employee_username_entry = tk.Entry(self, textvariable=self.employee_username_text)
        self.employee_username_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Employee Password
        self.employee_password_text = tk.StringVar()
        self.employee_password_label = tk.Label(self, text='Password: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.employee_password_entry = tk.Entry(self, textvariable=self.employee_password_text)
        self.employee_password_entry.grid(row=2, column=4)
        tk.Label(self, text="                                                                                                              ").grid(row=2, column=5, columnspan=4)

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

        # Employee List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_login_list = tk.Listbox(self, height=7, width=130, border=1)
        self.employee_login_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeCredentialRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_login_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_login_list.yview)

        # Bind select
        self.employee_login_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.employee_login_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.employee_login_list.get(index)

            # Display data at entry box
            self.employee_username_entry.delete(0, tk.END)
            self.employee_username_entry.insert(tk.END, self.selected_item[1])
            self.employee_password_entry.delete(0, tk.END)
            self.employee_password_entry.insert(tk.END, self.selected_item[2])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.employee_username_text.get() == '' or self.employee_password_text.get() =='':            
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        inputData = (self.employee_username_text.get(), self.employee_password_text.get())
        employeeLoginDB.insert(inputData)

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        employeeLoginDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        employeeLoginDB.update(self.selected_item[0], self.employee_username_text.get(), self.employee_password_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.employee_username_entry.delete(0, tk.END)
        self.employee_password_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_login_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeLoginDB.fetch():
            line = [row[0], row[1], row[2]]
            self.employee_login_list.insert(tk.END, line)


# Employee License Record Window
class EmployeeLicenseRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee license record page element
        self.header = tk.Label(self, text="Employee License Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Employee License Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_license_list = tk.Listbox(self, height=15, width=130, border=1)
        self.employee_license_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit License", height="1", width="15", command=lambda: controller.show_frame(EmployeeLicense)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit License Number", height="1", width="17", command=lambda: controller.show_frame(EmployeeLicenseNumber)).grid(row=11, column=3, sticky=tk.W)
        tk.Button(self, text="Edit Employee", height="1", width="15", command=lambda: controller.show_frame(Employee)).grid(row=11, column=4, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_license_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_license_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_license_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeCredentialRecordDB.fetch():
            self.employee_license_list.insert(tk.END, row)


# Employee License Window
class EmployeeLicense(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee license page element
        self.header = tk.Label(self, text="Employee License Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Employee ID
        self.employeeid_text = tk.StringVar()
        self.employeeid_label = tk.Label(self, text='Employee ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.employeeid_entry = tk.Entry(self, textvariable=self.employeeid_text)
        self.employeeid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Employee Status ID
        self.employeestatusid_text = tk.StringVar()
        self.employeestatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.employeestatusid_entry = tk.Entry(self, textvariable=self.employeestatusid_text)
        self.employeestatusid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Employee Type ID 
        self.employeetypeid_text = tk.StringVar()
        self.employeetypeid_label = tk.Label(self, text='Type ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.employeetypeid_entry = tk.Entry(self, textvariable=self.employeetypeid_text)
        self.employeetypeid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Employee License Number ID
        self.employeelicensenumberid_text = tk.StringVar()
        self.employeelicensenumberid_label = tk.Label(self, text='Number ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.employeelicensenumberid_entry = tk.Entry(self, textvariable=self.employeelicensenumberid_text)
        self.employeelicensenumberid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

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

        # employee List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_license_list = tk.Listbox(self, height=7, width=130, border=1)
        self.employee_license_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeLicenseRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_license_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_license_list.yview)

        # Bind select
        self.employee_license_list.bind('<<ListboxSelect>>', self.select_item)

        

    def select_item(self, event):
        try:
            # Get index
            index = self.employee_license_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.employee_license_list.get(index)

            # Display data at entry box
            self.employeeid_entry.delete(0, tk.END)
            self.employeeid_entry.insert(tk.END, self.selected_item[1])
            self.employeestatusid_entry.delete(0, tk.END)
            self.employeestatusid_entry.insert(tk.END, self.selected_item[2])
            self.employeetypeid_entry.delete(0, tk.END)
            self.employeetypeid_entry.insert(tk.END, self.selected_item[3])
            self.employeelicensenumberid_entry.delete(0, tk.END)
            self.employeelicensenumberid_entry.insert(tk.END, self.selected_item[4])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.employeeid_text.get() == '' or self.employeestatusid_text.get() == '' or self.employeetypeid_text.get() == '' \
                                            or self.employeelicensenumberid_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        employeeLicenseDB.insert(self.employeeid_text.get(), self.employeestatusid_text.get(), self.employeetypeid_text.get(), 
                                self.employeelicensenumberid_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        employeeLicenseDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        employeeLicenseDB.update(self.selected_item[0], self.employeeid_text.get(), self.employeestatusid_text.get(), self.employeetypeid_text.get(), 
                                self.employeelicensenumberid_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.employeeid_entry.delete(0, tk.END)
        self.employeestatusid_entry.delete(0, tk.END)
        self.employeetypeid_entry.delete(0, tk.END)
        self.employeelicensenumberid_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_license_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeLicenseDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4]]
            self.employee_license_list.insert(tk.END, line)


# Employee License Number Window
class EmployeeLicenseNumber(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create employee license number page element
        self.header = tk.Label(self, text="Employee License Number Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Employee License Number
        self.employee_license_number_text = tk.StringVar()
        self.employee_license_number_label = tk.Label(self, text='License Number: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.employee_license_number_entry = tk.Entry(self, textvariable=self.employee_license_number_text)
        self.employee_license_number_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        tk.Label(self, text="                             ").grid(row=2, column=3)
        tk.Label(self, text="                                        ").grid(row=2, column=4)
        tk.Label(self, text="                                                                                       ").grid(row=2, column=5, columnspan=4)
        
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

        # Employee License Number List
        tk.Label(self, text="").grid(row=7, column=0)
        self.employee_license_number_list = tk.Listbox(self, height=7, width=130, border=1)
        self.employee_license_number_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EmployeeLicenseRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.employee_license_number_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.employee_license_number_list.yview)

        # Bind select
        self.employee_license_number_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.employee_license_number_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.employee_license_number_list.get(index)

            # Display data at entry box
            self.employee_license_number_entry.delete(0, tk.END)
            self.employee_license_number_entry.insert(tk.END, self.selected_item[1])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.employee_license_number_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        employeeLicenseNumberDB.insert(self.employee_license_number_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        employeeLicenseNumberDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        employeeLicenseNumberDB.update(self.selected_item[0], self.employee_license_number_text.get())
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.employee_license_number_entry.delete(0, tk.END)
        self.employee_license_number_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.employee_license_number_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in employeeLicenseNumberDB.fetch():
            line = [row[0], row[1]]
            self.employee_license_number_list.insert(tk.END, line)


# ------------------------------------------- COURSE ------------------------------------------------ 

# Course Record Window
class CourseRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create course record page element
        self.header = tk.Label(self, text="Course Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Course Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.course_list = tk.Listbox(self, height=15, width=130, border=1)
        self.course_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(CourseDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="15", command=lambda: controller.show_frame(Course)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.course_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.course_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.course_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in courseRecordDB.fetch():
            self.course_list.insert(tk.END, row)


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
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(CourseRecord)).grid(row=11, column=1, sticky=tk.W)

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
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                    row[7], row[8]]
            self.courses_list.insert(tk.END, line)


# Student Course Status Record Window
class StudentCourseStatusRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create student course status record page element
        self.header = tk.Label(self, text="Student Course Status Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Student Course Status Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.student_course_status_list = tk.Listbox(self, height=15, width=130, border=1)
        self.student_course_status_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(CourseDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="15", command=lambda: controller.show_frame(StudentCourseStatus)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_course_status_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_course_status_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_course_status_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentCourseStatusRecordDB.fetch():
            self.student_course_status_list.insert(tk.END, row)


# Student Course Status Window
class StudentCourseStatus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create course page element
        self.header = tk.Label(self, text="Student Course Status Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)

        # Store selected item
        self.selected_item = 0
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Course ID
        self.courseid_text = tk.StringVar()
        self.courseid_label = tk.Label(self, text='Course ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.courseid_entry = tk.Entry(self, textvariable=self.courseid_text)
        self.courseid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Student Category ID
        self.studentcategoryid_text = tk.StringVar()
        self.studentcategoryid_label = tk.Label(self, text='Category ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.studentcategoryid_entry = tk.Entry(self, textvariable=self.studentcategoryid_text)
        self.studentcategoryid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Student Code ID
        self.studentcodeid_text = tk.StringVar()
        self.studentcodeid_label = tk.Label(self, text='Code ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.studentcodeid_entry = tk.Entry(self, textvariable=self.studentcodeid_text)
        self.studentcodeid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Student Course Status
        self.student_course_status_text = tk.StringVar()
        self.student_course_status_label = tk.Label(self, text='Student Status: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.student_course_status_entry = tk.Entry(self, textvariable=self.student_course_status_text)
        self.student_course_status_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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
        self.student_course_status_list = tk.Listbox(self, height=7, width=130, border=1)
        self.student_course_status_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(StudentCourseStatusRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.student_course_status_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.student_course_status_list.yview)

        # Bind select
        self.student_course_status_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.student_course_status_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.student_course_status_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.courseid_entry.delete(0, tk.END)
            self.courseid_entry.insert(tk.END, self.selected_item[2])
            self.studentcategoryid_entry.delete(0, tk.END)
            self.studentcategoryid_entry.insert(tk.END, self.selected_item[3])
            self.studentcodeid_entry.delete(0, tk.END)
            self.studentcodeid_entry.insert(tk.END, self.selected_item[4])
            self.student_course_status_entry.delete(0, tk.END)
            self.student_course_status_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.courseid_text.get() == '' or self.studentcategoryid_text.get() == '' \
                                            or self.studentcodeid_text.get() == '' or self.student_course_status_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        studentCourseStatusDB.insert(self.studentid_text.get(), self.courseid_text.get(), self.studentcategoryid_text.get(),
                                    self.studentcodeid_text.get(), self.student_course_status_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        studentCourseStatusDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        studentCourseStatusDB.update(self.selected_item[0], self.studentid_text.get(), self.courseid_text.get(),
                                    self.studentcategoryid_text.get(), self.studentcodeid_text.get(),
                                    self.student_course_status_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.courseid_entry.delete(0, tk.END)
        self.studentcategoryid_entry.delete(0, tk.END)
        self.studentcodeid_entry.delete(0, tk.END)
        self.student_course_status_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.student_course_status_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in studentCourseStatusDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.student_course_status_list.insert(tk.END, line)


# ------------------------------------------- INVENTORY ------------------------------------------------ 

# Merchandise Record Window
class MerchandiseRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership record page element
        self.header = tk.Label(self, text="Merchandise Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Merchandise Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.merchandise_list = tk.Listbox(self, height=15, width=130, border=1)
        self.merchandise_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(InventoryDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Merchandise Record Button
        tk.Button(self, text="Edit Merchandise", height="1", width="15", command=lambda: controller.show_frame(Merchandise)).grid(row=11, column=2, sticky=tk.W)

        # Edit Vendor Record Button
        tk.Button(self, text="Edit Vendor", height="1", width="10", command=lambda: controller.show_frame(VendorRecord)).grid(row=11, column=3, sticky=tk.W)   # Need Update

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.merchandise_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.merchandise_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.merchandise_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in merchandiseRecordDB.fetch():
            self.merchandise_list.insert(tk.END, row)


# Merchandise Window
class Merchandise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create merchandise page element
        self.header = tk.Label(self, text="Merchandise Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Vendor ID
        self.vendorid_text = tk.StringVar()
        self.vendorid_label = tk.Label(self, text='Vendor ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.vendorid_entry = tk.Entry(self, textvariable=self.vendorid_text)
        self.vendorid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Merchandise Type ID
        self.merchandisetypeid_text = tk.StringVar()
        self.merchandisetypeid_label = tk.Label(self, text='Type ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.merchandisetypeid_entry = tk.Entry(self, textvariable=self.merchandisetypeid_text)
        self.merchandisetypeid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Merchandise Number ID
        self.merchandisenumberid_text = tk.StringVar()
        self.merchandisenumberid_label = tk.Label(self, text='Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.merchandisenumberid_entry = tk.Entry(self, textvariable=self.merchandisenumberid_text)
        self.merchandisenumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Merchandise Status ID
        self.merchandisestatusid_text = tk.StringVar()
        self.merchandisestatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.merchandisestatusid_entry = tk.Entry(self, textvariable=self.merchandisestatusid_text)
        self.merchandisestatusid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Merchandise Name
        self.merchandise_name_text = tk.StringVar()
        self.merchandise_name_label = tk.Label(self, text='Merchandise Name: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.merchandise_name_entry = tk.Entry(self, textvariable=self.merchandise_name_text)
        self.merchandise_name_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Merchandise Price
        self.merchandise_price_text = tk.StringVar()
        self.merchandise_price_label = tk.Label(self, text='Merchandise Price: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.merchandise_price_entry = tk.Entry(self, textvariable=self.merchandise_price_text)
        self.merchandise_price_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Merchandise List
        tk.Label(self, text="").grid(row=7, column=0)
        self.merchandise_list = tk.Listbox(self, height=7, width=130, border=1)
        self.merchandise_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(MerchandiseRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.merchandise_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.merchandise_list.yview)

        # Bind select
        self.merchandise_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.merchandise_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.merchandise_list.get(index)

            # Display data at entry box
            self.vendorid_entry.delete(0, tk.END)
            self.vendorid_entry.insert(tk.END, self.selected_item[1])
            self.merchandisetypeid_entry.delete(0, tk.END)
            self.merchandisetypeid_entry.insert(tk.END, self.selected_item[2])
            self.merchandisenumberid_entry.delete(0, tk.END)
            self.merchandisenumberid_entry.insert(tk.END, self.selected_item[3])
            self.merchandisestatusid_entry.delete(0, tk.END)
            self.merchandisestatusid_entry.insert(tk.END, self.selected_item[4])
            self.merchandise_name_entry.delete(0, tk.END)
            self.merchandise_name_entry.insert(tk.END, self.selected_item[5])
            self.merchandise_price_entry.delete(0, tk.END)
            self.merchandise_price_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.vendorid_text.get() == '' or self.merchandisetypeid_text.get() == '' or self.merchandisenumberid_text.get() == '' \
                                            or self.merchandisestatusid_text.get() == '' or self.merchandise_name_text.get() == '' \
                                            or self.merchandise_price_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        merchandiseDB.insert(self.vendorid_text.get(), self.merchandisetypeid_text.get(), self.merchandisenumberid_text.get(),
                        self.merchandisestatusid_text.get(), self.merchandise_name_text.get(), self.merchandise_price_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")        


    def remove_item(self):
        # Pass in the ID of selected item
        merchandiseDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        merchandiseDB.update(self.selected_item[0], self.vendorid_text.get(), self.merchandisetypeid_text.get(), self.merchandisenumberid_text.get(),
                        self.merchandisestatusid_text.get(), self.merchandise_name_text.get(), self.merchandise_price_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.vendorid_entry.delete(0, tk.END)
        self.merchandisetypeid_entry.delete(0, tk.END)
        self.merchandisenumberid_entry.delete(0, tk.END)
        self.merchandisestatusid_entry.delete(0, tk.END)
        self.merchandise_name_entry.delete(0, tk.END)
        self.merchandise_price_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.merchandise_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in merchandiseDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.merchandise_list.insert(tk.END, line)


# Equipment Record Window
class EquipmentRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create equipment record page element
        self.header = tk.Label(self, text="Equipment Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Equipment Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.equipment_list = tk.Listbox(self, height=15, width=130, border=1)
        self.equipment_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(InventoryDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Equipment Record Button
        tk.Button(self, text="Edit Equipment", height="1", width="15", command=lambda: controller.show_frame(Equipment)).grid(row=11, column=2, sticky=tk.W)

        # Edit Vendor Record Button
        tk.Button(self, text="Edit Vendor", height="1", width="10", command=lambda: controller.show_frame(VendorRecord)).grid(row=11, column=3, sticky=tk.W)   # Need Update

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.equipment_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.equipment_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.equipment_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in equipmentRecordDB.fetch():
            self.equipment_list.insert(tk.END, row)


# Equipment Window
class Equipment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership page element
        self.header = tk.Label(self, text="Equipment Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Vendor ID
        self.vendorid_text = tk.StringVar()
        self.vendorid_label = tk.Label(self, text='Vendor ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.vendorid_entry = tk.Entry(self, textvariable=self.vendorid_text)
        self.vendorid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Equipment Type ID
        self.equipmenttypeid_text = tk.StringVar()
        self.equipmenttypeid_label = tk.Label(self, text='Type ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.equipmenttypeid_entry = tk.Entry(self, textvariable=self.equipmenttypeid_text)
        self.equipmenttypeid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Equipment Number ID
        self.equipmentnumberid_text = tk.StringVar()
        self.equipmentnumberid_label = tk.Label(self, text='Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.equipmentnumberid_entry = tk.Entry(self, textvariable=self.equipmentnumberid_text)
        self.equipmentnumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Equipment Status ID
        self.equipmentstatusid_text = tk.StringVar()
        self.equipmentstatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.equipmentstatusid_entry = tk.Entry(self, textvariable=self.equipmentstatusid_text)
        self.equipmentstatusid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Equipment Name
        self.equipment_name_text = tk.StringVar()
        self.equipment_name_label = tk.Label(self, text='Equipment Name: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.equipment_name_entry = tk.Entry(self, textvariable=self.equipment_name_text)
        self.equipment_name_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Equipment Price
        self.equipment_price_text = tk.StringVar()
        self.equipment_price_label = tk.Label(self, text='Equipment Price: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.equipment_price_entry = tk.Entry(self, textvariable=self.equipment_price_text)
        self.equipment_price_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Equipment List
        tk.Label(self, text="").grid(row=7, column=0)
        self.equipment_list = tk.Listbox(self, height=7, width=130, border=1)
        self.equipment_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EquipmentRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.equipment_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.equipment_list.yview)

        # Bind select
        self.equipment_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.equipment_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.equipment_list.get(index)

            # Display data at entry box
            self.vendorid_entry.delete(0, tk.END)
            self.vendorid_entry.insert(tk.END, self.selected_item[1])
            self.equipmenttypeid_entry.delete(0, tk.END)
            self.equipmenttypeid_entry.insert(tk.END, self.selected_item[2])
            self.equipmentnumberid_entry.delete(0, tk.END)
            self.equipmentnumberid_entry.insert(tk.END, self.selected_item[3])
            self.equipmentstatusid_entry.delete(0, tk.END)
            self.equipmentstatusid_entry.insert(tk.END, self.selected_item[4])
            self.equipment_name_entry.delete(0, tk.END)
            self.equipment_name_entry.insert(tk.END, self.selected_item[5])
            self.equipment_price_entry.delete(0, tk.END)
            self.equipment_price_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.vendorid_text.get() == '' or self.equipmenttypeid_text.get() == '' or self.equipmentnumberid_text.get() == '' \
                                                or self.equipmentstatusid_text.get() == '' or self.equipment_name_text.get() == '' \
                                                or self.equipment_price_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        equipmentDB.insert(self.vendorid_text.get(), self.equipmenttypeid_text.get(), self.equipmentnumberid_text.get(),
                        self.equipmentstatusid_text.get(), self.equipment_name_text.get(), self.equipment_price_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")        


    def remove_item(self):
        # Pass in the ID of selected item
        equipmentDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        equipmentDB.update(self.selected_item[0], self.vendorid_text.get(), self.equipmenttypeid_text.get(), self.equipmentnumberid_text.get(),
                        self.equipmentstatusid_text.get(), self.equipment_name_text.get(), self.equipment_price_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
        

    # Clear entry box
    def clear_text(self):
        self.vendorid_entry.delete(0, tk.END)
        self.equipmenttypeid_entry.delete(0, tk.END)
        self.equipmentnumberid_entry.delete(0, tk.END)
        self.equipmentstatusid_entry.delete(0, tk.END)
        self.equipment_name_entry.delete(0, tk.END)
        self.equipment_price_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.equipment_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in equipmentDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.equipment_list.insert(tk.END, line)

      
# ------------------------------------------- MEMBERSHIP ------------------------------------------------ 

# Membership Record Window
class MembershipRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership record page element
        self.header = tk.Label(self, text="Membership Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Membership Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.membership_list = tk.Listbox(self, height=15, width=130, border=1)
        self.membership_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Membership)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.membership_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.membership_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.membership_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in membershipRecordDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            self.membership_list.insert(tk.END, line)


# Membership Window
class Membership(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create membership page element
        self.header = tk.Label(self, text="Membership Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Membership Status ID
        self.membershipstatusid_text = tk.StringVar()
        self.membershipstatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.membershipstatusid_entry = tk.Entry(self, textvariable=self.membershipstatusid_text)
        self.membershipstatusid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Membership Number ID
        self.membershipnumberid_text = tk.StringVar()
        self.membershipnumberid_label = tk.Label(self, text='Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.membershipnumberid_entry = tk.Entry(self, textvariable=self.membershipnumberid_text)
        self.membershipnumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Membership Type ID
        self.membershiptypeid_text = tk.StringVar()
        self.membershiptypeid_label = tk.Label(self, text='Type ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.membershiptypeid_entry = tk.Entry(self, textvariable=self.membershiptypeid_text)
        self.membershiptypeid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Membership Fee
        self.membership_fee_text = tk.StringVar()
        self.membership_fee_label = tk.Label(self, text='Membership Fee: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.membership_fee_entry = tk.Entry(self, textvariable=self.membership_fee_text)
        self.membership_fee_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Start Date
        self.membership_start_date_text = tk.StringVar()
        self.membership_start_date_label = tk.Label(self, text='Start Date: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.membership_start_date_entry = tk.Entry(self, textvariable=self.membership_start_date_text)
        self.membership_start_date_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

        # End Date
        self.membership_end_date_text = tk.StringVar()
        self.membership_end_date_label = tk.Label(self, text='End Date: ', font=("Segoe UI", 11)).grid(row=4, column=0, sticky=tk.W)
        self.membership_end_date_entry = tk.Entry(self, textvariable=self.membership_end_date_text)
        self.membership_end_date_entry.grid(row=4, column=1)
        tk.Label(self, text="          ").grid(row=4, column=2)

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

        # Membership List
        tk.Label(self, text="").grid(row=7, column=0)
        self.membership_list = tk.Listbox(self, height=7, width=130, border=1)
        self.membership_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(MembershipRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.membership_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.membership_list.yview)

        # Bind select
        self.membership_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.membership_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.membership_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.membershipstatusid_entry.delete(0, tk.END)
            self.membershipstatusid_entry.insert(tk.END, self.selected_item[2])
            self.membershipnumberid_entry.delete(0, tk.END)
            self.membershipnumberid_entry.insert(tk.END, self.selected_item[3])
            self.membershiptypeid_entry.delete(0, tk.END)
            self.membershiptypeid_entry.insert(tk.END, self.selected_item[4])
            self.membership_fee_entry.delete(0, tk.END)
            self.membership_fee_entry.insert(tk.END, self.selected_item[5])
            self.membership_start_date_entry.delete(0, tk.END)
            self.membership_start_date_entry.insert(tk.END, self.selected_item[6])
            self.membership_end_date_entry.delete(0, tk.END)
            self.membership_end_date_entry.insert(tk.END, self.selected_item[7])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.membershipstatusid_text.get() == '' or self.membershipnumberid_text.get() == '' \
                                            or self.membershiptypeid_text.get() == '' or self.membership_fee_text.get() == '' \
                                            or self.membership_start_date_text.get() == '' or self.membership_end_date_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        membershipDB.insert(self.studentid_text.get(), self.membershipstatusid_text.get(), self.membershipnumberid_text.get(),
                        self.membershiptypeid_text.get(), self.membership_fee_text.get(), self.membership_start_date_text.get(),
                        self.membership_end_date_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        membershipDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        membershipDB.update(self.selected_item[0], self.studentid_text.get(), self.membershipstatusid_text.get(), self.membershipnumberid_text.get(),
                        self.membershiptypeid_text.get(), self.membership_fee_text.get(), self.membership_start_date_text.get(),
                        self.membership_end_date_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.membershipstatusid_entry.delete(0, tk.END)
        self.membershipnumberid_entry.delete(0, tk.END)
        self.membershiptypeid_entry.delete(0, tk.END)
        self.membership_fee_entry.delete(0, tk.END)
        self.membership_start_date_entry.delete(0, tk.END)
        self.membership_end_date_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.membership_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in membershipDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
            self.membership_list.insert(tk.END, line)


# ------------------------------------------- ENROLLMENT ------------------------------------------------

# Enrollment Record Window
class EnrollmentRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create enrollment record page element
        self.header = tk.Label(self, text="Enrollment Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Enrollment Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.enrollment_list = tk.Listbox(self, height=15, width=130, border=1)
        self.enrollment_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Enrollment)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.enrollment_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.enrollment_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.enrollment_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in enrollmentRecordDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.enrollment_list.insert(tk.END, line)


# Enrollment Window
class Enrollment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create enrollment page element
        self.header = tk.Label(self, text="Enrollment Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Enrollment Status ID
        self.enrollmentstatusid_text = tk.StringVar()
        self.enrollmentstatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.enrollmentstatusid_entry = tk.Entry(self, textvariable=self.enrollmentstatusid_text)
        self.enrollmentstatusid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Enrollment Number ID
        self.enrollmentnumberid_text = tk.StringVar()
        self.enrollmentnumberid_label = tk.Label(self, text='Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.enrollmentnumberid_entry = tk.Entry(self, textvariable=self.enrollmentnumberid_text)
        self.enrollmentnumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Enrollment Period ID
        self.enrollmentperiodid_text = tk.StringVar()
        self.enrollmentperiodid_label = tk.Label(self, text='Period ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.enrollmentperiodid_entry = tk.Entry(self, textvariable=self.enrollmentperiodid_text)
        self.enrollmentperiodid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Enrollment Date
        self.enrollment_date_text = tk.StringVar()
        self.enrollment_date_label = tk.Label(self, text='Membership Fee: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.enrollment_date_entry = tk.Entry(self, textvariable=self.enrollment_date_text)
        self.enrollment_date_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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

        # Membership List
        tk.Label(self, text="").grid(row=7, column=0)
        self.enrollment_list = tk.Listbox(self, height=7, width=130, border=1)
        self.enrollment_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EnrollmentRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.enrollment_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.enrollment_list.yview)

        # Bind select
        self.enrollment_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.enrollment_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.enrollment_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.enrollmentstatusid_entry.delete(0, tk.END)
            self.enrollmentstatusid_entry.insert(tk.END, self.selected_item[2])
            self.enrollmentnumberid_entry.delete(0, tk.END)
            self.enrollmentnumberid_entry.insert(tk.END, self.selected_item[3])
            self.enrollmentperiodid_entry.delete(0, tk.END)
            self.enrollmentperiodid_entry.insert(tk.END, self.selected_item[4])
            self.enrollment_date_entry.delete(0, tk.END)
            self.enrollment_date_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.enrollmentstatusid_text.get() == '' or self.enrollmentnumberid_text.get() == '' \
                                            or self.enrollmentperiodid_text.get() == '' or self.enrollment_date_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        enrollmentDB.insert(self.studentid_text.get(), self.enrollmentstatusid_text.get(), self.enrollmentnumberid_text.get(),
                        self.enrollmentperiodid_text.get(), self.enrollment_date_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        enrollmentDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        enrollmentDB.update(self.selected_item[0], self.studentid_text.get(), self.enrollmentstatusid_text.get(), self.enrollmentnumberid_text.get(),
                        self.enrollmentperiodid_text.get(), self.enrollment_date_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.enrollmentstatusid_entry.delete(0, tk.END)
        self.enrollmentnumberid_entry.delete(0, tk.END)
        self.enrollmentperiodid_entry.delete(0, tk.END)
        self.enrollment_date_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.enrollment_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in enrollmentDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.enrollment_list.insert(tk.END, line)


# ------------------------------------------- EVENT -----------------------------------------------------

# Event Record Window
class EventRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create event record page element
        self.header = tk.Label(self, text="Event Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Event Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.event_list = tk.Listbox(self, height=15, width=130, border=1)
        self.event_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EventDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit Event", height="1", width="15", command=lambda: controller.show_frame(Event)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Event Status", height="1", width="15", command=lambda: controller.show_frame(EventStatus)).grid(row=11, column=3, sticky=tk.W)
        tk.Button(self, text="Edit Dance Team", height="1", width="15", command=lambda: controller.show_frame(DanceTeam)).grid(row=11, column=4, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.event_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.event_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.event_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in eventRecordDB.fetch():
            self.event_list.insert(tk.END, row)


# Event Window
class Event(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create event page element
        self.header = tk.Label(self, text="Event Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Event Status ID
        self.eventstatusid_text = tk.StringVar()
        self.eventstatusid_label = tk.Label(self, text='Event Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.eventstatusid_entry = tk.Entry(self, textvariable=self.eventstatusid_text)
        self.eventstatusid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Dance Team ID
        self.danceteamid_text = tk.StringVar()
        self.danceteamid_label = tk.Label(self, text='Dance Team ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.danceteamid_entry = tk.Entry(self, textvariable=self.danceteamid_text)
        self.danceteamid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Event Number ID
        self.eventnumberid_text = tk.StringVar()
        self.eventnumberid_label = tk.Label(self, text='Event Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.eventnumberid_entry = tk.Entry(self, textvariable=self.eventnumberid_text)
        self.eventnumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Event Period ID
        self.eventperiodid_text = tk.StringVar()
        self.eventperiodid_label = tk.Label(self, text='Event Period ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.eventperiodid_entry = tk.Entry(self, textvariable=self.eventperiodid_text)
        self.eventperiodid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Event Name
        self.event_name_text = tk.StringVar()
        self.event_name_label = tk.Label(self, text='Event Name: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.event_name_entry = tk.Entry(self, textvariable=self.event_name_text)
        self.event_name_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

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

        # Event List
        tk.Label(self, text="").grid(row=7, column=0)
        self.event_list = tk.Listbox(self, height=7, width=130, border=1)
        self.event_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EventRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.event_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.event_list.yview)

        # Bind select
        self.event_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.event_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.event_list.get(index)

            # Display data at entry box
            self.eventstatusid_entry.delete(0, tk.END)
            self.eventstatusid_entry.insert(tk.END, self.selected_item[1])
            self.danceteamid_entry.delete(0, tk.END)
            self.danceteamid_entry.insert(tk.END, self.selected_item[2])
            self.eventnumberid_entry.delete(0, tk.END)
            self.eventnumberid_entry.insert(tk.END, self.selected_item[3])
            self.eventperiodid_entry.delete(0, tk.END)
            self.eventperiodid_entry.insert(tk.END, self.selected_item[4])
            self.event_name_entry.delete(0, tk.END)
            self.event_name_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.eventstatusid_text.get() == '' or self.danceteamid_text.get() == '' or self.eventnumberid_text.get() == '' \
                                                or self.eventperiodid_text.get() == '' or self.event_name_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        eventDB.insert(self.eventstatusid_text.get(), self.danceteamid_text.get(), self.eventnumberid_text.get(),
                    self.eventperiodid_text.get(), self.event_name_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        eventDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        eventDB.update(self.selected_item[0], self.eventstatusid_text.get(), self.danceteamid_text.get(), self.eventnumberid_text.get(),
                    self.eventperiodid_text.get(), self.event_name_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.eventstatusid_entry.delete(0, tk.END)
        self.danceteamid_entry.delete(0, tk.END)
        self.eventnumberid_entry.delete(0, tk.END)
        self.eventperiodid_entry.delete(0, tk.END)
        self.event_name_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.event_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in eventDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5]]
            self.event_list.insert(tk.END, line)


# Event Status Window
class EventStatus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create event status page element
        self.header = tk.Label(self, text="Event Status Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Event Status
        self.event_status_text = tk.StringVar()
        self.event_status_label = tk.Label(self, text='Event Status: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.event_status_entry = tk.Entry(self, textvariable=self.event_status_text)
        self.event_status_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Event Start Date
        self.event_start_date_text = tk.StringVar()
        self.event_start_date_label = tk.Label(self, text='Event Start Date: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.event_start_date_entry = tk.Entry(self, textvariable=self.event_start_date_text)
        self.event_start_date_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Event End Date
        self.event_end_date_text = tk.StringVar()
        self.event_end_date_label = tk.Label(self, text='Event End Date: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.event_end_date_entry = tk.Entry(self, textvariable=self.event_end_date_text)
        self.event_end_date_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

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

        # Event List
        tk.Label(self, text="").grid(row=7, column=0)
        self.event_status_list = tk.Listbox(self, height=7, width=130, border=1)
        self.event_status_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EventRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.event_status_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.event_status_list.yview)

        # Bind select
        self.event_status_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.event_status_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.event_status_list.get(index)

            # Display data at entry box
            self.event_status_entry.delete(0, tk.END)
            self.event_status_entry.insert(tk.END, self.selected_item[1])
            self.event_start_date_entry.delete(0, tk.END)
            self.event_start_date_entry.insert(tk.END, self.selected_item[2])
            self.event_end_date_entry.delete(0, tk.END)
            self.event_end_date_entry.insert(tk.END, self.selected_item[3])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.event_status_text.get() == '' or self.event_start_date_text.get() == '' or self.event_end_date_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        eventStatusDB.insert(self.event_status_text.get(), self.event_start_date_text.get(), self.event_end_date_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        eventStatusDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        eventStatusDB.update(self.selected_item[0], self.event_status_text.get(), self.event_start_date_text.get(), self.event_end_date_text.get())
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.event_status_entry.delete(0, tk.END)
        self.event_start_date_entry.delete(0, tk.END)
        self.event_end_date_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.event_status_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in eventStatusDB.fetch():
            line = [row[0], row[1], row[2], row[3]]
            self.event_status_list.insert(tk.END, line)


# Dance Team Window
class DanceTeam(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create dance team page element
        self.header = tk.Label(self, text="Dance Team Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Dance Team Name
        self.dance_team_text = tk.StringVar()
        self.dance_team_label = tk.Label(self, text='Dance Team: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.dance_team_entry = tk.Entry(self, textvariable=self.dance_team_text)
        self.dance_team_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        tk.Label(self, text="                             ").grid(row=2, column=3)
        tk.Label(self, text="                                        ").grid(row=2, column=4)
        tk.Label(self, text="                                                                                       ").grid(row=2, column=5, columnspan=4)

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

        # Dance Team List
        tk.Label(self, text="").grid(row=7, column=0)
        self.dance_team_list = tk.Listbox(self, height=7, width=130, border=1)
        self.dance_team_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EventRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.dance_team_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.dance_team_list.yview)

        # Bind select
        self.dance_team_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.dance_team_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.dance_team_list.get(index)

            # Display data at entry box
            self.dance_team_entry.delete(0, tk.END)
            self.dance_team_entry.insert(tk.END, self.selected_item[1])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.dance_team_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        danceTeamDB.insert(self.dance_team_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        danceTeamDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        danceTeamDB.update(self.selected_item[0], self.dance_team_text.get())
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.dance_team_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.dance_team_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in danceTeamDB.fetch():
            line = [row[0], row[1]]
            self.dance_team_list.insert(tk.END, line)


# Reservation Record Window
class ReservationRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create reservation record page element
        self.header = tk.Label(self, text="Reservation Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Reservation Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.reservation_list = tk.Listbox(self, height=15, width=130, border=1)
        self.reservation_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(EventDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit Reservation", height="1", width="15", command=lambda: controller.show_frame(Reservation)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Dance Team", height="1", width="15", command=lambda: controller.show_frame(DanceTeam)).grid(row=11, column=3, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.reservation_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.reservation_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.reservation_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in reservationRecordDB.fetch():
            self.reservation_list.insert(tk.END, row)


# Reservation Window
class Reservation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create reservation page element
        self.header = tk.Label(self, text="Reservation Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Event ID
        self.eventid_text = tk.StringVar()
        self.eventid_label = tk.Label(self, text='Event ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.eventid_entry = tk.Entry(self, textvariable=self.eventid_text)
        self.eventid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Reservation Number ID
        self.reservationnumberid_text = tk.StringVar()
        self.reservationnumberid_label = tk.Label(self, text='Reservation Number ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.reservationnumberid_entry = tk.Entry(self, textvariable=self.reservationnumberid_text)
        self.reservationnumberid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Dance Team ID
        self.danceteamid_text = tk.StringVar()
        self.danceteamid_label = tk.Label(self, text='Dance Team ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.danceteamid_entry = tk.Entry(self, textvariable=self.danceteamid_text)
        self.danceteamid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Description
        self.reservation_description_text = tk.StringVar()
        self.reservation_description_label = tk.Label(self, text='Description: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.reservation_description_entry = tk.Entry(self, textvariable=self.reservation_description_text)
        self.reservation_description_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Reservation Date
        self.reservation_date_text = tk.StringVar()
        self.reservation_date_label = tk.Label(self, text='Reservation Date: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.reservation_date_entry = tk.Entry(self, textvariable=self.reservation_date_text)
        self.reservation_date_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Reservation List
        tk.Label(self, text="").grid(row=7, column=0)
        self.reservation_list = tk.Listbox(self, height=7, width=130, border=1)
        self.reservation_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(ReservationRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.reservation_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.reservation_list.yview)

        # Bind select
        self.reservation_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.reservation_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.reservation_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.eventid_entry.delete(0, tk.END)
            self.eventid_entry.insert(tk.END, self.selected_item[2])
            self.reservationnumberid_entry.delete(0, tk.END)
            self.reservationnumberid_entry.insert(tk.END, self.selected_item[3])
            self.danceteamid_entry.delete(0, tk.END)
            self.danceteamid_entry.insert(tk.END, self.selected_item[4])
            self.reservation_description_entry.delete(0, tk.END)
            self.reservation_description_entry.insert(tk.END, self.selected_item[5])
            self.reservation_date_entry.delete(0, tk.END)
            self.reservation_date_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.eventid_text.get() == '' or self.reservationnumberid_text.get() == '' \
                                            or self.danceteamid_text.get() == '' or self.reservation_description_text.get() == '' \
                                            or self.reservation_date_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        reservationDB.insert(self.studentid_text.get(), self.eventid_text.get(), self.reservationnumberid_text.get(), self.danceteamid_text.get(),
                            self.reservation_description_text.get(), self.reservation_date_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        reservationDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        reservationDB.update(self.selected_item[0], self.studentid_text.get(), self.eventid_text.get(), self.reservationnumberid_text.get(), self.danceteamid_text.get(),
                            self.reservation_description_text.get(), self.reservation_date_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.eventid_entry.delete(0, tk.END)
        self.reservationnumberid_entry.delete(0, tk.END)
        self.danceteamid_entry.delete(0, tk.END)
        self.reservation_description_entry.delete(0, tk.END)
        self.reservation_date_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.reservation_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in reservationDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.reservation_list.insert(tk.END, line)


# ------------------------------------------- BILL ------------------------------------------------------

# Bill Record Window
class BillRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create bill record page element
        self.header = tk.Label(self, text="Bill Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Bill Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.bill_list = tk.Listbox(self, height=15, width=130, border=1)
        self.bill_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Bill)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.bill_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.bill_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.bill_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in billRecordDB.fetch():
            self.bill_list.insert(tk.END, row)


# Bill Window
class Bill(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create bill page element
        self.header = tk.Label(self, text="Bill Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(self, text='Student ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(self, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Course Price ID
        self.coursepriceid_text = tk.StringVar()
        self.coursepriceid_label = tk.Label(self, text='Course Price ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.coursepriceid_entry = tk.Entry(self, textvariable=self.coursepriceid_text)
        self.coursepriceid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Membership ID
        self.membershipid_text = tk.StringVar()
        self.membershipid_label = tk.Label(self, text='Membership ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.membershipid_entry = tk.Entry(self, textvariable=self.membershipid_text)
        self.membershipid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Membership Type ID
        self.billnumberid_text = tk.StringVar()
        self.billnumberid_label = tk.Label(self, text='Bill Number ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.billnumberid_entry = tk.Entry(self, textvariable=self.billnumberid_text)
        self.billnumberid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Bill Date
        self.bill_date_text = tk.StringVar()
        self.bill_date_label = tk.Label(self, text='Bill Date: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.bill_date_entry = tk.Entry(self, textvariable=self.bill_date_text)
        self.bill_date_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Total Bill
        self.total_bill_text = tk.StringVar()
        self.total_bill_label = tk.Label(self, text='Total Bill: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.total_bill_entry = tk.Entry(self, textvariable=self.total_bill_text)
        self.total_bill_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Bill List
        tk.Label(self, text="").grid(row=7, column=0)
        self.bill_list = tk.Listbox(self, height=7, width=130, border=1)
        self.bill_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(BillRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.bill_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.bill_list.yview)

        # Bind select
        self.bill_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.bill_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.bill_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.coursepriceid_entry.delete(0, tk.END)
            self.coursepriceid_entry.insert(tk.END, self.selected_item[2])
            self.membershipid_entry.delete(0, tk.END)
            self.membershipid_entry.insert(tk.END, self.selected_item[3])
            self.billnumberid_entry.delete(0, tk.END)
            self.billnumberid_entry.insert(tk.END, self.selected_item[4])
            self.bill_date_entry.delete(0, tk.END)
            self.bill_date_entry.insert(tk.END, self.selected_item[5])
            self.total_bill_entry.delete(0, tk.END)
            self.total_bill_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.studentid_text.get() == '' or self.coursepriceid_text.get() == '' or self.membershipid_text.get() == '' \
                                            or self.billnumberid_text.get() == '' or self.bill_date_text.get() == '' \
                                            or self.total_bill_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        billDB.insert(self.studentid_text.get(), self.coursepriceid_text.get(), self.membershipid_text.get(),
                    self.billnumberid_text.get(), self.bill_date_text.get(), self.total_bill_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        billDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        billDB.update(self.selected_item[0], self.studentid_text.get(), self.coursepriceid_text.get(), self.membershipid_text.get(),
                    self.billnumberid_text.get(), self.bill_date_text.get(), self.total_bill_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.coursepriceid_entry.delete(0, tk.END)
        self.membershipid_entry.delete(0, tk.END)
        self.billnumberid_entry.delete(0, tk.END)
        self.bill_date_entry.delete(0, tk.END)
        self.total_bill_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.bill_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in billDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.bill_list.insert(tk.END, line)


# ------------------------------------------- Admin ------------------------------------------------------

# Admin Record Window
class AdminRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create admin record page element
        self.header = tk.Label(self, text="Admin Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Admin Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.admin_list = tk.Listbox(self, height=15, width=130, border=1)
        self.admin_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(AdminDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit All", height="1", width="15", command=lambda: controller.show_frame(Admin)).grid(row=11, column=2, sticky=tk.W)
        tk.Button(self, text="Edit Admin Info", height="1", width="15", command=lambda: controller.show_frame(AdminInfo)).grid(row=11, column=3, sticky=tk.W)
        tk.Button(self, text="Edit Admin Login", height="1", width="15", command=lambda: controller.show_frame(AdminLogin)).grid(row=11, column=4, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.admin_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.admin_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.admin_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in adminRecordDB.fetch():
            self.admin_list.insert(tk.END, row)


# Admin Window
class Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create admin page element
        self.header = tk.Label(self, text="Admin Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Admin Info ID
        self.admininfoid_text = tk.StringVar()
        self.admininfoid_label = tk.Label(self, text='Admin Info ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.admininfoid_entry = tk.Entry(self, textvariable=self.admininfoid_text)
        self.admininfoid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Admin Login ID
        self.adminloginid_text = tk.StringVar()
        self.adminloginid_label = tk.Label(self, text='Admin Login ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.adminloginid_entry = tk.Entry(self, textvariable=self.adminloginid_text)
        self.adminloginid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # Admin Status ID
        self.adminstatusid_text = tk.StringVar()
        self.adminstatusid_label = tk.Label(self, text='Admin Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.adminstatusid_entry = tk.Entry(self, textvariable=self.adminstatusid_text)
        self.adminstatusid_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Address ID
        self.addressid_text = tk.StringVar()
        self.addressid_label = tk.Label(self, text='Address ID: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.addressid_entry = tk.Entry(self, textvariable=self.addressid_text)
        self.addressid_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

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

        # Admin List
        tk.Label(self, text="").grid(row=7, column=0)
        self.admin_list = tk.Listbox(self, height=7, width=130, border=1)
        self.admin_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(AdminRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.admin_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.admin_list.yview)

        # Bind select
        self.admin_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.admin_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.admin_list.get(index)

            # Display data at entry box
            self.admininfoid_entry.delete(0, tk.END)
            self.admininfoid_entry.insert(tk.END, self.selected_item[1])
            self.adminloginid_entry.delete(0, tk.END)
            self.adminloginid_entry.insert(tk.END, self.selected_item[2])
            self.adminstatusid_entry.delete(0, tk.END)
            self.adminstatusid_entry.insert(tk.END, self.selected_item[3])
            self.addressid_entry.delete(0, tk.END)
            self.addressid_entry.insert(tk.END, self.selected_item[4])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.admininfoid_text.get() == '' or self.adminloginid_text.get() == '' or self.adminstatusid_text.get() == '' or self.addressid_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        adminDB.insert(self.admininfoid_text.get(), self.adminloginid_text.get(), self.adminstatusid_text.get(), self.addressid_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        adminDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        adminDB.update(self.selected_item[0], self.admininfoid_text.get(), self.adminloginid_text.get(), self.adminstatusid_text.get(), self.addressid_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.admininfoid_entry.delete(0, tk.END)
        self.adminloginid_entry.delete(0, tk.END)
        self.adminstatusid_entry.delete(0, tk.END)
        self.addressid_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.admin_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in adminDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4]]
            self.admin_list.insert(tk.END, line)


# Admin Info Window
class AdminInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create admin info page element
        self.header = tk.Label(self, text="Admin Info Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # First Name
        self.first_name_text = tk.StringVar()
        self.first_name_label = tk.Label(self, text='First Name: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Last Name
        self.last_name_text = tk.StringVar()
        self.last_name_label = tk.Label(self, text='Last Name: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_entry.grid(row=2, column=4)
        tk.Label(self, text="                                                                                                              ").grid(row=2, column=5, columnspan=4)

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

        # Admin Info List
        tk.Label(self, text="").grid(row=7, column=0)
        self.admin_info_list = tk.Listbox(self, height=7, width=130, border=1)
        self.admin_info_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(AdminRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.admin_info_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.admin_info_list.yview)

        # Bind select
        self.admin_info_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.admin_info_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.admin_info_list.get(index)

            # Display data at entry box
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(tk.END, self.selected_item[1])
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(tk.END, self.selected_item[2])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.first_name_text.get() == '' or self.last_name_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        adminInfoDB.insert(self.first_name_text.get(), self.last_name_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        adminInfoDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        adminInfoDB.update(self.selected_item[0], self.first_name_text.get(), self.last_name_text.get())
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.admin_info_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in adminInfoDB.fetch():
            line = [row[0], row[1], row[2]]
            self.admin_info_list.insert(tk.END, line)


# Admin Login Window
class AdminLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create admin login page element
        self.header = tk.Label(self, text="Admin Login Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Admin Username
        self.adminusername_text = tk.StringVar()
        self.adminusername_label = tk.Label(self, text='Admin Username: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.adminusername_entry = tk.Entry(self, textvariable=self.adminusername_text)
        self.adminusername_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Admin Password
        self.adminpassword_text = tk.StringVar()
        self.adminpassword_label = tk.Label(self, text='Admin Password: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.adminpassword_entry = tk.Entry(self, textvariable=self.adminpassword_text)
        self.adminpassword_entry.grid(row=2, column=4)
        tk.Label(self, text="                                                                                                              ").grid(row=2, column=5, columnspan=4)

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

        # Admin List
        tk.Label(self, text="").grid(row=7, column=0)
        self.admin_login_list = tk.Listbox(self, height=7, width=130, border=1)
        self.admin_login_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(AdminRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.admin_login_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.admin_login_list.yview)

        # Bind select
        self.admin_login_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.admin_login_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.admin_login_list.get(index)

            # Display data at entry box
            self.adminusername_entry.delete(0, tk.END)
            self.adminusername_entry.insert(tk.END, self.selected_item[1])
            self.adminpassword_entry.delete(0, tk.END)
            self.adminpassword_entry.insert(tk.END, self.selected_item[2])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.adminusername_text.get() == '' or self.adminpassword_text.get() =='':            
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        inputData = (self.adminusername_text.get(), self.adminpassword_text.get())
        adminLoginDB.insert(inputData)

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        adminLoginDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        adminLoginDB.update(self.selected_item[0], self.adminusername_text.get(), self.adminpassword_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.adminusername_entry.delete(0, tk.END)
        self.adminpassword_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.admin_login_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in adminLoginDB.fetch():
            line = [row[0], row[1], row[2]]
            self.admin_login_list.insert(tk.END, line)


# Owner Record Window
class OwnerRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create owner record page element
        self.header = tk.Label(self, text="Owner Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Owner Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.owner_list = tk.Listbox(self, height=15, width=130, border=1)
        self.owner_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(AdminDashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Owner)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.owner_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.owner_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.owner_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in ownerRecordDB.fetch():
            self.owner_list.insert(tk.END, row)


# Bill Window
class Owner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create owner page element
        self.header = tk.Label(self, text="Owner Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Address ID
        self.addressid_text = tk.StringVar()
        self.addressid_label = tk.Label(self, text='Address ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.addressid_entry = tk.Entry(self, textvariable=self.addressid_text)
        self.addressid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Owner Status ID
        self.ownerstatusid_text = tk.StringVar()
        self.ownerstatusid_label = tk.Label(self, text='Owner Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.ownerstatusid_entry = tk.Entry(self, textvariable=self.ownerstatusid_text)
        self.ownerstatusid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # First Name
        self.first_name_text = tk.StringVar()
        self.first_name_label = tk.Label(self, text='First Name: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Last Name
        self.last_name_text = tk.StringVar()
        self.last_name_label = tk.Label(self, text='Last Name: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Phone
        self.phone_text = tk.StringVar()
        self.phone_label = tk.Label(self, text='Phone: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.phone_entry = tk.Entry(self, textvariable=self.phone_text)
        self.phone_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Email
        self.email_text = tk.StringVar()
        self.email_label = tk.Label(self, text='Email: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.email_entry = tk.Entry(self, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Membership List
        tk.Label(self, text="").grid(row=7, column=0)
        self.owner_list = tk.Listbox(self, height=7, width=130, border=1)
        self.owner_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(OwnerRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.owner_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.owner_list.yview)

        # Bind select
        self.owner_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.owner_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.owner_list.get(index)

            # Display data at entry box
            self.addressid_entry.delete(0, tk.END)
            self.addressid_entry.insert(tk.END, self.selected_item[1])
            self.ownerstatusid_entry.delete(0, tk.END)
            self.ownerstatusid_entry.insert(tk.END, self.selected_item[2])
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(tk.END, self.selected_item[3])
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(tk.END, self.selected_item[4])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, self.selected_item[5])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.addressid_text.get() == '' or self.ownerstatusid_text.get() == '' or self.first_name_text.get() == '' \
                                            or self.last_name_text.get() == '' or self.phone_text.get() == '' \
                                            or self.email_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return
        
        # Insert into database
        ownerDB.insert(self.addressid_text.get(), self.ownerstatusid_text.get(), self.first_name_text.get(),
                    self.last_name_text.get(), self.phone_text.get(), self.email_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()


    def remove_item(self):
        # Pass in the ID of selected item
        ownerDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        ownerDB.update(self.selected_item[0], self.addressid_text.get(), self.ownerstatusid_text.get(), self.first_name_text.get(),
                    self.last_name_text.get(), self.phone_text.get(), self.email_text.get())
        
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")
       
        
    # Clear entry box
    def clear_text(self):
        self.addressid_entry.delete(0, tk.END)
        self.ownerstatusid_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.owner_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in ownerDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.owner_list.insert(tk.END, line)


# ------------------------------------------- VENDOR ----------------------------------------------------

# Vendor Record Window
class VendorRecord(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create vendor record page element
        self.header = tk.Label(self, text="Vendor Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()

    
    def create_widgets(self, controller):

        # No Entry and Buttons Needed: Read-only Table

        # Vendor Record List
        tk.Label(self, text="").grid(row=7, column=0)
        self.vendor_list = tk.Listbox(self, height=15, width=130, border=1)
        self.vendor_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=1, sticky=tk.W)

        # Edit Record Button
        tk.Button(self, text="Edit", height="1", width="10", command=lambda: controller.show_frame(Vendor)).grid(row=11, column=2, sticky=tk.W)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.vendor_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.vendor_list.yview)

        
    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.vendor_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in vendorRecordDB.fetch():
            self.vendor_list.insert(tk.END, row)


# Vendor Window
class Vendor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create vendor page element
        self.header = tk.Label(self, text="Vendor Records", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=9)   # The first parameter: where to put the element
        tk.Label(self, text="").grid(row=1, column=0)

        # Create widgets
        self.create_widgets(controller)
        
        # Populate initial list
        self.populate_list()


    def create_widgets(self, controller):
        # Address ID
        self.addressid_text = tk.StringVar()
        self.addressid_label = tk.Label(self, text='Address ID: ', font=("Segoe UI", 11)).grid(row=2, column=0, sticky=tk.W)
        self.addressid_entry = tk.Entry(self, textvariable=self.addressid_text)
        self.addressid_entry.grid(row=2, column=1)
        tk.Label(self, text="          ").grid(row=2, column=2)
        
        # Vendor Status ID
        self.vendorstatusid_text = tk.StringVar()
        self.vendorstatusid_label = tk.Label(self, text='Status ID: ', font=("Segoe UI", 11)).grid(row=2, column=3, sticky=tk.W)
        self.vendorstatusid_entry = tk.Entry(self, textvariable=self.vendorstatusid_text)
        self.vendorstatusid_entry.grid(row=2, column=4)
        tk.Label(self, text="          ").grid(row=2, column=5)

        # First Name
        self.first_name_text = tk.StringVar()
        self.first_name_label = tk.Label(self, text='First Name: ', font=("Segoe UI", 11)).grid(row=2, column=6, sticky=tk.W)
        self.first_name_entry = tk.Entry(self, textvariable=self.first_name_text)
        self.first_name_entry.grid(row=2, column=7)
        tk.Label(self, text="          ").grid(row=2, column=8)

        # Last Name
        self.last_name_text = tk.StringVar()
        self.last_name_label = tk.Label(self, text='Last Name: ', font=("Segoe UI", 11)).grid(row=3, column=0, sticky=tk.W)
        self.last_name_entry = tk.Entry(self, textvariable=self.last_name_text)
        self.last_name_entry.grid(row=3, column=1)
        tk.Label(self, text="          ").grid(row=3, column=2)

        # Phone
        self.phone_text = tk.StringVar()
        self.phone_label = tk.Label(self, text='Phone: ', font=("Segoe UI", 11)).grid(row=3, column=3, sticky=tk.W)
        self.phone_entry = tk.Entry(self, textvariable=self.phone_text)
        self.phone_entry.grid(row=3, column=4)
        tk.Label(self, text="          ").grid(row=3, column=5)

        # Email
        self.email_text = tk.StringVar()
        self.email_label = tk.Label(self, text='Email: ', font=("Segoe UI", 11)).grid(row=3, column=6, sticky=tk.W)
        self.email_entry = tk.Entry(self, textvariable=self.email_text)
        self.email_entry.grid(row=3, column=7)
        tk.Label(self, text="          ").grid(row=3, column=8)

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

        # Vendor List
        tk.Label(self, text="").grid(row=7, column=0)
        self.vendor_list = tk.Listbox(self, height=7, width=130, border=1)
        self.vendor_list.grid(row=8, column=0, columnspan=8, rowspan=2)

        # Create Scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=8, column=8, rowspan=3)
        tk.Label(self, text="").grid(row=10, column=0)

        # Home Dashboard Button
        tk.Button(self, text="Home", height="1", width="10", command=lambda: controller.show_frame(Dashboard)).grid(row=11, column=0, sticky=tk.W)

        # Parent Dashboard Button
        tk.Button(self, text="Back", height="1", width="10", command=lambda: controller.show_frame(VendorRecord)).grid(row=11, column=1, sticky=tk.W)

        # Notification Label
        self.notification_label = tk.Label(self, text="", fg='green3', font=("Segoe UI", 11, "italic"))
        self.notification_label.grid(row=11, column=3, sticky=tk.W, columnspan=4)

        # Logout Button
        tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=11, column=7, sticky=tk.E)

        # Set Scroll to Listbox
        self.vendor_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.vendor_list.yview)

        # Bind select
        self.vendor_list.bind('<<ListboxSelect>>', self.select_item)

        
    def select_item(self, event):
        try:
            # Get index
            index = self.vendor_list.curselection()[0]
            
            # Get selected item
            self.selected_item = self.vendor_list.get(index)

            # Display data at entry box
            self.addressid_entry.delete(0, tk.END)
            self.addressid_entry.insert(tk.END, self.selected_item[1])
            self.vendorstatusid_entry.delete(0, tk.END)
            self.vendorstatusid_entry.insert(tk.END, self.selected_item[2])
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(tk.END, self.selected_item[3])
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(tk.END, self.selected_item[4])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, self.selected_item[5])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.selected_item[6])

        except IndexError:
            pass
    

    # Add new item to the DB
    def add_item(self):
        # Prevent empty input
        if self.addressid_text.get() == '' or self.vendorstatusid_text.get() == '' or self.first_name_text.get() == '' \
                                            or self.last_name_text.get() == '' or self.phone_text.get() == '' \
                                            or self.email_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return

        # Insert into database
        vendorDB.insert(self.addressid_text.get(), self.vendorstatusid_text.get(), self.first_name_text.get(),
                        self.last_name_text.get(), self.phone_text.get(), self.email_text.get())

        # Clear entry box
        self.clear_text()

        # Reload the listbox
        self.populate_list()

        # Show the message
        self.notification_label.config(text="New record has been added successfully!")


    def remove_item(self):
        # Pass in the ID of selected item
        vendorDB.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been deleted successfully!")


    def update_item(self):
        vendorDB.update(self.selected_item[0], self.addressid_text.get(), self.vendorstatusid_text.get(), self.first_name_text.get(),
                        self.last_name_text.get(), self.phone_text.get(), self.email_text.get())    

        self.clear_text()
        self.populate_list()
        self.notification_label.config(text="Selected record has been updated successfully!")


    # Clear entry box
    def clear_text(self):
        self.addressid_entry.delete(0, tk.END)
        self.vendorstatusid_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.vendor_list.delete(0, tk.END)

        # Iterate through the data returned by the fetch method in Database Class
        for row in vendorDB.fetch():
            line = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            self.vendor_list.insert(tk.END, line)


# Start App
if __name__ == "__main__":
    app = App()
    app.run()