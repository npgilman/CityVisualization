# python file to drive GUI interactions
import json
from PIL import Image as IMG
from PIL import ImageTk as ImagTK
from tkinter import *

window = Tk(screenName="City Visualization")
window.resizable(False, False)
window.geometry("800x600")
window.title("City Visualization")

controlFrame = Frame(window, width=200, height=600, bg="green")
displayFrame = Frame(window, width=600, bg="red")

controlFrame.pack(fill=BOTH, side=LEFT)
displayFrame.pack(fill=BOTH, side=LEFT)

pixel = PhotoImage(width=1, height=1)
generateButton = Button(controlFrame, image=pixel, width=200, height=50, text="Visualize State!", compound="c")
generateButton.pack(side=BOTTOM)

# Dropdown menu options
options = []

data = None
with open('states.json') as states:
    data = json.load(states)

for (State, Info) in data.items():
    options.append(State)

# drop down menu
clicked = StringVar()
clicked.set("Florida")
drop = OptionMenu(controlFrame , clicked , *options)
drop.pack(fill=BOTH)

pngString = "PNGres/" + data[clicked.get()]['State_ID'] + ".png"
pngString = "PNGres/IN.png"
image = IMG.open(pngString)
display = ImagTK.PhotoImage(image)
global label2 
label2 = Label(displayFrame, image=display)
label2.pack(fill=BOTH, side=LEFT)

# button function. add functionality
def show(event, label2 = label2):
    label2.destroy()
    pngString = "PNGres/" + data[clicked.get()]['State_ID'] + ".png"
    image = IMG.open(pngString)
    display = ImagTK.PhotoImage(image)
    label2 = Label(displayFrame, image=display)
    label2.pack(fill=BOTH, side=LEFT)
    print("Attempting to show " + pngString)

generateButton.bind("<Button-1>", show)



window.mainloop()