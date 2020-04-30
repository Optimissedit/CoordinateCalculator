# Sam Blawski 2020/4/29
#import pyperclip as pc (reminder to use this eventually...)
from tkinter import *
import math

# Creating and setting initial values for GUI window
window = Tk()

window.title("Coordinate Calculator")
window.geometry("450x100") #TODO: find true size to use
window.resizable(0,0)


# X Y Z Overworld Coordinate input boxes
xin = Entry(window, width = 10, bd = 3, justify= CENTER)
xin.insert(0, 0)
yin = Entry(window, width = 10, bd = 3, justify= CENTER)
yin.insert(0,0)
zin = Entry(window, width = 10, bd = 3, justify= CENTER)
zin.insert(0,0)

# Grid positions for XYZ (Overworld)
xin.grid(column = 0, row = 2)
yin.grid(column = 1, row = 2)
zin.grid(column = 2, row = 2)


# X Y Z Nether Coordinate input boxes
xout = Entry(window, width=10, bd=3, justify=CENTER)
xout.insert(0, 0)
yout = Entry(window, width=10, bd=3, justify=CENTER)
yout.insert(0, 0)
zout = Entry(window, width=10, bd=3, justify=CENTER)
zout.insert(0, 0)

# Grid positions for XYZ (Overworld)
xout.grid(column = 4, row = 2)
yout.grid(column = 5, row = 2)
zout.grid(column = 6, row = 2)


# Labels to provide information on the window
equal_lbl = Label(window, text=" = ")
xinlbl = Label(window, text="X")
yinlbl = Label(window, text="Y")
zinlbl = Label(window, text="Z")
overlbl = Label(window, text="Overworld")

#Nether side labels
xoutlbl = Label(window, text="X")
youtlbl = Label(window, text="Y")
zoutlbl = Label(window, text="Z")
netherlbl = Label(window, text="Nether")


# Label grid positions
xinlbl.grid(column=0, row=1)
yinlbl.grid(column=1, row=1)
zinlbl.grid(column=2, row=1)
equal_lbl.grid(column = 3, row = 2)
overlbl.grid(column = 1, row = 0)

# Nether label grid pos
xoutlbl.grid(column=4, row=1)
youtlbl.grid(column=5, row=1)
zoutlbl.grid(column=6, row=1)
netherlbl.grid(column=5, row = 0)

#Button Functions
def translatecoords():
    xout.delete(0, 'end')
    xout.insert(0, math.floor((int(xin.get()) / 8)))
    zout.delete(0, 'end')
    zout.insert(0, math.floor((int(zin.get()) / 8)))
    yout.delete(0, 'end')
    yout.insert(0, yin.get())

#Button definition
translatebtn = Button(window, text="Calculate!", command=translatecoords)

#Button grid pos
translatebtn.grid(column = 1, row = 3)
# Run the program!
window.mainloop()