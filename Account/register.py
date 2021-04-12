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
    
