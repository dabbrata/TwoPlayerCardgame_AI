from subprocess import call
from tkinter import *
from PIL import ImageTk,Image

def quit():
    root.destroy()

def Run_Game_Mode():
    quit()
    call(["pythonw","run_game.py"])


root = Tk()  # create root window
root.title("Crad Game")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.geometry("500x400")
root.config(bg="skyblue")  # specify background color

# Create left and right frames
frame = Frame(root, width=1000, height=400,bg='skyblue')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

image = PhotoImage(file="card2.png")
btnstart = Image.open("start.png")
btnexit = Image.open("exit.png")
resized = btnstart.resize((150,50))
resizedex = btnexit.resize((150,50))
btnstart2 = ImageTk.PhotoImage(resized)
btnexit2 = ImageTk.PhotoImage(resizedex)

original_image = image.subsample(2,2)  # resize image using subsample
Label(frame, image=original_image,bg='skyblue').grid(row=0, column=1, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(frame, text="Start Game",font=("Arial", 20),fg='gray20',bg="skyblue").grid(row=1, column=1, padx=5, pady=5)
Button(frame,image=btnstart2,command=Run_Game_Mode,borderwidth="0",bg="skyblue").grid(row=3, column=1, padx=5, pady=3, ipadx=10)
Button(frame,command=quit, image=btnexit2,borderwidth="0",bg="skyblue").grid(row=4, column=1, padx=5, pady=3, ipadx=10)

root,mainloop()