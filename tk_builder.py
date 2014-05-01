#import Tkinter as tkinter      # for python2
import tkinter                  # for python3

#Encoding Magic
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

#other imports
import re

pd = PyDecipher(asl_encoding)

top = tkinter.Tk()

settingsFrame = tkinter.Frame(top)
settingsFrame.pack( side = tkinter.TOP )

# Add Blender Executable Text Entry
# Add Blender File Text Entry
# Add Python File Text Entry

# ==== BUILDING ====
builderFrame = tkinter.Frame(top)
builderFrame.pack( side = tkinter.BOTTOM )

codeFrame = tkinter.Frame(builderFrame)
codeFrame.pack( side = tkinter.LEFT )

code = tkinter.Text(codeFrame, fg="white", bg="black", state=tkinter.DISABLED, height=30, width=20)
code.pack( side = tkinter.TOP )

entry = tkinter.Text(codeFrame, fg="white", bg="black", state=tkinter.DISABLED, bd=5, height=1, width=20)
entry.pack( side = tkinter.BOTTOM )

# ==== RENDERING ====
renderFrame = tkinter.Frame(builderFrame)
renderFrame.pack( side = tkinter.RIGHT )

partsFrame = tkinter.Frame(renderFrame, bg="blue")
partsFrame.pack( side = tkinter.TOP )

pictureFrame = tkinter.Frame(renderFrame, bg="white")
pictureFrame.pack( side = tkinter.BOTTOM )

# ==== BIND-FUNCTIONS ====

top.buildString = ""
top.isValidString = False
def tkValidate(event):
    if ord(event.char) in [8, 13, 48, 49]:
        entry.config(state=tkinter.NORMAL)
        # Change the BuildString
        if len(top.buildString) > 0:
            entry.delete(1.0, tkinter.END)
        if ord(event.char) in [48, 49]:      # entered 0 or 1
            top.buildString += event.char
        elif ord(event.char) == 8:          # entered BACKSPACE
            top.buildString = top.buildString[:-1]

        # Create human-readble-ish string
        readString = top.buildString #TODO MORE STUFF HERE
        # Commit the BuildString
        elif ord(event.char) == 13:         # entered RETURN
            if (top.isValidString):
                code.config(state=tkinter.NORMAL)
                code.insert(tkinter.END, top.buildString)
                code.config(state=tkinter.DISABLED)

        # Check if BuildString is Valid
        if (pd.isValid(
        entry.insert(tkinter.INSERT, top.buildString)
        entry.config(state=tkinter.DISABLED)



top.bind("<Key>", tkValidate)

top.mainloop()
