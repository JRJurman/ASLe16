#import Tkinter as tkinter      # for python2
import tkinter                  # for python3

# Encoding Magic
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

# Other imports
import re

# Initialize PyDecipher object
pd = PyDecipher(asl_encoding)

# Run tk window
top = tkinter.Tk()
top.title("Interactive Builder")

# Colors
fgColor = "navajo white"
bgColor = "azure2"
bg2Color = "azure3"
validColor = "green4"
errorColor = "chocolate2"
detailColor = "DeepSkyBlue4"

# Defualt Height
lineHeight = 16

# ==== BUILDING ====
builderFrame = tkinter.Frame(top, bg=bg2Color)
builderFrame.pack( side = tkinter.BOTTOM )

codeFrame = tkinter.Frame(builderFrame)
codeFrame.pack( side = tkinter.LEFT )

entry = tkinter.Text(codeFrame, fg=fgColor, bg=bgColor, state=tkinter.DISABLED, font=(None, 16), bd=5, height=lineHeight, width=17)
entry.pack( side = tkinter.TOP )


# ==== RENDERING ====
renderFrame = tkinter.Frame( builderFrame, bg=bg2Color)
renderFrame.pack( side = tkinter.RIGHT )

partsFrame = tkinter.Frame( renderFrame, bg=bg2Color )
partsFrame.pack( side = tkinter.TOP )

output = tkinter.Text(partsFrame, fg=detailColor, bg=bgColor, state=tkinter.DISABLED, font=("helvetica",16), bd=5, height=lineHeight, width=25)
output.pack( side = tkinter.BOTTOM )

pictureFrame = tkinter.Frame(renderFrame, bg=bg2Color)
pictureFrame.pack( side = tkinter.BOTTOM )

# ==== BIND-FUNCTIONS ====

top.buildString = ""
top.isValidString = False
def tkValidate(event):
    if ord(event.char) in [8, 48, 49]:
        entry.config(state=tkinter.NORMAL)
        entry.delete(1.0, tkinter.END)
        # Change the BuildString
        if ord(event.char) in [48, 49]:      # entered 0 or 1
            top.buildString += event.char
        if ord(event.char) == 8:          # entered BACKSPACE
            top.buildString = top.buildString[:-1]
    
        # Create human-readble-ish string
        readString = " ".join( i for i in re.findall("([01]{,8})",top.buildString) if i != "")

        # Check if BuildString is Valid
        if (pd.isValid(readString)):
            top.isValidString = True
            entry.config(fg=validColor)
        else:
            entry.config(fg=errorColor)
        entry.insert(tkinter.INSERT, readString)
        entry.config(state=tkinter.DISABLED)

        # Print errors or parts in the output pane
        output.config(state=tkinter.NORMAL)
        output.delete(1.0, tkinter.END)
        parts = pd.decipher(top.buildString)
        res = ""
        for p in parts:
            res += "{}\n".format(p["name"])
            for m in p["modifiers"]:
                res += "| {} : {}\n".format(m[0], m[1])
        output.insert(tkinter.INSERT, res)
        output.config(state=tkinter.DISABLED)




top.bind("<Key>", tkValidate)

top.mainloop()
