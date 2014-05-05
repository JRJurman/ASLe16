#import Tkinter as tkinter      # for python2
import tkinter                  # for python3

# Encoding Magic
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

# Regex Library -- to do string formating
import re

# OS Libraries -- to do system calls
import subprocess, os

# Create a defualt render
if ( os.name == "nt" ): #WINDOWS SYSTEM
    pass

elif ( os.name == "posix" ): #MACOSX/LINUX/CYGWIN
    pass

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

# SELECTING FRAME
selectFrame = tkinter.Frame( top, bg=bg2Color )
selectFrame.pack( side = tkinter.LEFT )

binaryField = tkinter.Text( selectFrame, fg=validColor, bg=bgColor, state=tkinter.DISABLED, font=(None, 16), height=1, width=17 )
binaryField.pack( side = tkinter.TOP, anchor = "w")

dropDownFields = tkinter.Frame( selectFrame, bg=bg2Color )
dropDownFields.pack( side = tkinter.TOP )


# RENDER FRAME
renderFrame = tkinter.Frame( top, bg=bg2Color )
renderFrame.pack( side = tkinter.RIGHT )

# Preparing Lists
top.buildingBlocks = []

def newBlock():

    block = {}
    block["entry"] = tkinter.Frame( dropDownFields, bg=bgColor )
    block["entry"].pack( side = tkinter.TOP, anchor = "w" )
    block["PartStringVar"] = tkinter.StringVar()
    partName = sorted(asl_encoding.keys())[0]
    block["PartStringVar"].set( partName )
    block["ModifiersDropDown"] = []
    block["ModifiersLabel"] = []
    block["ModifiersStringVar"] = []

    top.buildingBlocks.append(block)
    binaryField.config( height = len(top.buildingBlocks) )
    setBlock(len(top.buildingBlocks)-1, partName)
    

def setBlock(index, partName):
    block = top.buildingBlocks[index]

    block["PartStringVar"].set( partName )
    block["PartDropDown"] = tkinter.OptionMenu( block["entry"], block["PartStringVar"], *sorted(asl_encoding.keys()),
                                                command=lambda e: setBlock(index, e))
    block["PartDropDown"].grid( row = 0, column = 0 )

    for m in block["ModifiersDropDown"]:
        m.destroy()
    for l in block["ModifiersLabel"]:
        l.destroy()
    block["ModifiersDropDown"] = []
    block["ModifiersLabel"] = []
    block["ModifiersStringVar"] = []
    col_val = 1
    for m in asl_encoding[partName].modifiers:
        block["ModifiersLabel"].append( tkinter.Label( block["entry"], bg=bgColor, text=m.name ) )
        block["ModifiersLabel"][-1].grid( row = 0, column = col_val )
        block["ModifiersStringVar"].append( tkinter.StringVar() )
        block["ModifiersStringVar"][-1].set( sorted(m.values.values())[0] )
        block["ModifiersDropDown"].append(tkinter.OptionMenu( block["entry"], block["ModifiersStringVar"][-1], *sorted(m.values.values()), command=render ))
        block["ModifiersDropDown"][-1].grid( row = 0, column = col_val+1 )
        col_val += 2
        
    top.buildingBlocks[index] = block
    render(None)


def render(event):
    buildString = ""
    pCount = len(top.buildingBlocks)-1
    for p in top.buildingBlocks:
        if pCount != 0:
            buildString += "1"
            pCount -= 1
        else:
            buildString += "0"

        partName = p["PartStringVar"].get()
        part = asl_encoding[partName]
        partId = part.identifier
        buildString += "{} ".format(partId)
        for mi in range(len(asl_encoding[partName].modifiers)): 
            m = asl_encoding[partName].modifiers[mi]
            mId = m.reverseLookup[p["ModifiersStringVar"][mi].get()]
            buildString += mId

    binaryField.config( state = tkinter.NORMAL )
    binaryField.delete( "1.0", tkinter.END )
    binaryField.insert( "1.0", buildString )
    binaryField.config( state = tkinter.DISABLED )

newBlock()

addButton = tkinter.Button( selectFrame, text="+", bg=bgColor, command=newBlock )
addButton.pack( side = tkinter.BOTTOM )


top.mainloop()
