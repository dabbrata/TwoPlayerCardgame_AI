import tkinter as tk
import sys
import os
from tkinter import *
from subprocess import call
from PIL import ImageTk,Image

def quit():
    root.destroy()


def open_hexenzirkel_file():
    quit()
    call(["python","Hexenzirkel_Beta_Version.py"])

root = tk.Tk()
root.title("HEXENZIRKEL(easy)")
root.geometry("300x300")
root.config(bg="skyblue")


btnexit = Image.open("exit2.png")
resizedex = btnexit.resize((150,60))
btnexit2 = ImageTk.PhotoImage(resizedex)

btnrestart = Image.open("restart.png")
resizedrestart = btnrestart.resize((115,45))
btnrestart2 = ImageTk.PhotoImage(resizedrestart)

right_frame = Frame(root, width=250, height=150, bg='skyblue')
right_frame.grid(row=0, column=1, padx=55, pady=55)

Label(right_frame, text="Do you want to exit or restart?",bg="skyblue",font=("Arial", 10),fg="red3",wraplength=100).grid(row=0, column=0, padx=5, pady=5)

Button(right_frame, image=btnrestart2,command=open_hexenzirkel_file, relief=RAISED,padx = "0",pady="0",borderwidth="0",bg="skyblue",fg="white",font=("Arial", 8)).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
Button(right_frame, image=btnexit2,command=quit, relief=RAISED,padx = "0",pady="0",borderwidth="0",bg="skyblue",fg="white",font=("Arial", 8)).grid(row=3, column=0, padx=5, pady=3, ipadx=10)


root.mainloop()