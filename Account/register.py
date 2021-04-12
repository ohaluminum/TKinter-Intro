import tkinter as tk
from tkinter import messagebox
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