from tkinter import *
from PIL import ImageTk, Image

def RegisterUser():
    usernameInfo = username.get()
    passwordInfo = password.get()
    
    # Validation: require 
    # Save it to database
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    
    Label(register, text="").pack()
    Label(register, text="Registration Success!", fg="green", font=("Segoe UI", 11, "italic")).pack()
    


def Register():
    # Create register window object
    global register
    register = Toplevel(main)
    register.title("Soundbox Dance Studios - Register")
    register.iconbitmap("logo_ico.ico")
    register.geometry("500x600")

    # Create register page element
    logoLabel = Label(register, image=knugenLogo).pack()
    registerTitle = Label(register, text="User Registration", font=("Segoe UI", 18, "bold")).pack()      # The first parameter: where to put the element

    global userType
    global username
    global password    
    global usernameEntry
    global passwordEntry

    userType = IntVar()
    username = StringVar()
    password = StringVar()

    Label(register, text="").pack()
    usernameLabel = Label(register, text="Username: ", font=("Segoe UI", 11)).pack()
    usernameEntry = Entry(register, textvariable=username)
    usernameEntry.pack()
    passwordLabel = Label(register, text="Password: ", font=("Segoe UI", 11)).pack()
    passwordEntry = Entry(register, textvariable=password)
    passwordEntry.pack()
    Label(register, text="").pack()
    adminRadioButton = Radiobutton(register, text="Administrator", variable=userType, value=1, font=("Segoe UI", 11)).pack()  #,  side=LEFT
    employeeRadioButton = Radiobutton(register, text="Employee", variable=userType, value=2, font=("Segoe UI", 11)).pack()
    Label(register, text="").pack()
    registerButton = Button(register, text="Register", height="2", width="15", font=("Segoe UI", 11), command=RegisterUser).pack()





def Login():
    print("login")

def MainPage():
    # Create main window object
    global main
    main = Tk()
    main.title("Soundbox Dance Studios - Welcome")
    main.iconbitmap("logo_ico.ico")
    main.geometry("500x400")

    # Create home page element
    global knugenLogo
    global logoLabel
    knugenLogo = ImageTk.PhotoImage((Image.open("logo_png.png")))
    logoLabel = Label(main, image=knugenLogo).pack()
    mainTitle = Label(main, text="Soundbox Dance Studios", font=("Segoe UI", 18, "bold")).pack()         # The first parameter: where to put the element

    Label(main, text="").pack()    # Equivalent to empty line 
    loginButton = Button(main, text="Login", height="2", width="15", command=Login).pack()
    Label(main, text="").pack()
    registerButton = Button(main, text="Register", height="2", width="15", command=Register).pack()

    main.mainloop()

MainPage()

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
