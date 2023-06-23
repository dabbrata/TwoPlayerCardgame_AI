from subprocess import call
from tkinter import *
from PIL import ImageTk,Image

def quit():
    root.destroy()


def open_hexenzirkel_file():
    quit()
    call(["python","Hexenzirkel_Beta_Version.py"])

def open_octakor_file():
    quit()
    call(["python","OctaKor_Beta_Version.py"])

def open_syvsirkel_file():
    quit()
    call(["python","SyvSirkel_Beta_Version.py"])


root = Tk()  # create root window
root.title("Crad Game")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="navajowhite2")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=300, height=400,bg='navajowhite2')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=650, height=400, bg='navajowhite2')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(right_frame, text="Welcome",bg="navajowhite2",font=("Arial", 25),fg="red3").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"
image = PhotoImage(file="card2.png")
#image for exit button
btnexit = Image.open("exit.png")
resizedex = btnexit.resize((140,40))
btnexit2 = ImageTk.PhotoImage(resizedex)

original_image = image.subsample(3,3)  # resize image using subsample
Label(right_frame, image=original_image,bg='navajowhite2').grid(row=1, column=0, padx=5, pady=5)

# Display image in left_frame
image_left = PhotoImage(file="left_grid_bg.png")
original_image_left = image_left.subsample(6,6)  # resize image using subsample
Label(left_frame, image=original_image_left,bg='navajowhite2').grid(row=1, column=0, padx=5, pady=5)
txt = "There are three different mode in the game .\nOne is hexenzirkel which is played with six cards.\nOther two " \
      "is syvSirkel and octacore \nwhich is played with seven and eight card respectively.\nThe rule is : There are 2 " \
      "players and the highest point achieving player will win the game. "
Label(left_frame, text=txt,bg='navajowhite2',wraplength="350").grid(row=2, column=0, padx=5, pady=5)
Button(left_frame,command=quit, image= btnexit2 ,relief=RAISED,padx = "40",pady="8",borderwidth="0",bg="navajowhite2",fg="white",font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5)  # ipadx is padding inside the Label widget


# Create tool bar frame
tool_bar = Frame(right_frame, width=180, height=185,bg="navajowhite2")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Select one mode of the game",font=("Arial", 12),fg="red4",bg='navajowhite2').grid(row=0, column=0, padx=5, pady=5)
Button(tool_bar, text="Easy",command=open_hexenzirkel_file, relief=SOLID,padx = "38",pady="10",borderwidth="0",bg="blue",fg="white",font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Button(tool_bar, text="Medium",command=open_syvsirkel_file, relief=SOLID,padx = "30",pady="10",borderwidth="0",bg="green",fg="white",font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
Button(tool_bar, text="Hard",command=open_octakor_file, relief=SOLID,padx = "40",pady="10",borderwidth="0",bg="red",fg="white",font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

# Example labels that could be displayed under the "Tool" menu

root.mainloop()


