import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Account.employee_login_db import EmployeeLoginDB
from Account.admin_login_db import AdminLoginDB


# Application Class
class Dashboard(tk.Tk):
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

        for F in (HomeDashboard, ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Display the current page
        self.show_frame(HomeDashboard)
    
    def show_frame(self, curr):
        frame = self.frames[curr]
        frame.tkraise()

    def run(self):
        self.mainloop()


# Dashboard Window
class HomeDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create dashboard page element
        #tk.Label(self, text="").grid(row=0, column=0)    # Equivalent to empty line
        #tk.Label(self, text="").grid(row=1, column=0)    # Equivalent to empty line
        self.header = tk.Label(self, text="Soundbox Studios Main Dashboard", font=("Segoe UI", 18, "bold")).grid(row=2, column=0, columnspan=12)   # The first parameter: where to put the element

        # 1. Student Button
        tk.Label(self, text="").grid(row=3, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=4, column=0)    # Equivalent to empty line
        self.studentButton = tk.Button(self, text="Student", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=5, column=0)

        # 2. Employee Button
        tk.Label(self, text="      ").grid(row=5, column=1)    # Equivalent to empty column
        self.employeeButton = tk.Button(self, text="Employee", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=5, column=2)

        # 3. Course Button
        tk.Label(self, text="      ").grid(row=5, column=3)    # Equivalent to empty column
        self.courseButton = tk.Button(self, text="Course", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=5, column=4)
        
        # 4. Inventory Button 
        tk.Label(self, text="      ").grid(row=5, column=5)    # Equivalent to empty column
        self.inverntoryButton = tk.Button(self, text="Inventory", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=5, column=6)
        
        # 5. Membership Button
        tk.Label(self, text="      ").grid(row=5, column=7)    # Equivalent to empty column
        self.membershipButton = tk.Button(self, text="Membership", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=5, column=8)
    
        # 6. Enrollment Button
        tk.Label(self, text="").grid(row=6, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=7, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=8, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=9, column=0)    # Equivalent to empty line
        self.enrollmentButton = tk.Button(self, text="Enrollment", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=10, column=0)

        # 7. Reservation/Event Button
        tk.Label(self, text="      ").grid(row=10, column=1)    # Equivalent to empty line
        self.eventButton = tk.Button(self, text="Reservation/Event", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=10, column=2)

        # 8. Bill Button
        tk.Label(self, text="      ").grid(row=10, column=3)    # Equivalent to empty line
        self.billButton = tk.Button(self, text="Bill Record", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=10, column=4)

        # 9. Admin/Owner Button
        tk.Label(self, text="      ").grid(row=10, column=5)    # Equivalent to empty line
        self.adminButton = tk.Button(self, text="Admin/Owner Information", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=10, column=6)

        # 10. Vendor Button
        tk.Label(self, text="      ").grid(row=10, column=7)    # Equivalent to empty line
        self.vendorButton = tk.Button(self, text="Vendor Information", height="3", width="20", command=lambda: controller.show_frame(Homepage)).grid(row=10, column=8)

        # 11. Logout Button
        tk.Label(self, text="").grid(row=11, column=0)    # Equivalent to empty line
        tk.Label(self, text="").grid(row=12, column=0)    # Equivalent to empty line
        self.logoutButton = tk.Button(self, text="Logout", height="1", width="10", command=lambda: controller.show_frame(Homepage)).grid(row=13, column=8, sticky=tk.E)

