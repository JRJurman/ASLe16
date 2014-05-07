import sys
if sys.version_info.major >= 3:
    import tkinter                  # for python3
else:
    import Tkinter as tkinter       # for python2

# Encoding Magic
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

# Regex Library -- to do string formating
import re

# OS Libraries -- to do system calls
import subprocess, os, shlex

# time library -- make sure that rendering doesn't take forever
import time

# Initialize PyDecipher object
pd = PyDecipher(asl_encoding)

# Run tk window
top = tkinter.Tk()
top.title("ASLe16 Interactive Builder")

# Colors
fgColor = "navajo white"
bgColor = "azure2"
bg2Color = "azure3"
validColor = "green4"
errorColor = "chocolate2"
detailColor = "DeepSkyBlue4"

# SELECTING FRAME
selectFrame = tkinter.Frame( top, bg=bg2Color )
selectFrame.pack( side = tkinter.LEFT, anchor = "nw" )

binaryField = tkinter.Text( selectFrame, fg=validColor, bg=bgColor, state=tkinter.DISABLED, font=(None, 16), height=1, width=17 )
binaryField.pack( side = tkinter.TOP, anchor = "w")

dropDownFields = tkinter.Frame( selectFrame, bg=bg2Color )
dropDownFields.pack( side = tkinter.TOP )


# RENDER FRAME
renderFrame = tkinter.Frame( top, bg=bg2Color )
renderFrame.pack( side = tkinter.RIGHT )

renderLabel = tkinter.Label( renderFrame )
renderLabel.pack()

#command = r'"C:\Program Files\Blender Foundation\Blender\blender.exe" -b "ASL_Model.blend" -P "blender_script.py" -y -o "tmp\asl" -F BMP -x 1 -f 1 -t 0 -noglsl'
command = [r"C:\Program Files\Blender Foundation\Blender\blender.exe","-b",'ASL_Model.blend',"-P","blender_script.py","-y","-o",r"tmp\asl","-F","BMP","-x","1","-f","1","-t","0","-noglsl"]
print(command)
blender_process = subprocess.Popen(command, stdin = subprocess.PIPE, shell=True)

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
    
def removeBlock(index=-1, event=None):

    block = top.buildingBlocks.pop(index)
    block["entry"].destroy()
    binaryField.config( height = len(top.buildingBlocks) )
    print(top.buildingBlocks)


    render(None)


def setBlock(index, partName):
    block = top.buildingBlocks[index]

    block["PartStringVar"].set( partName )
    block["PartDropDown"] = tkinter.OptionMenu( block["entry"], block["PartStringVar"], *sorted(asl_encoding.keys()),
                                                command=lambda e: setBlock(index, e))
    block["PartDropDown"].grid( row = 0, column = 2 )

    for m in block["ModifiersDropDown"]:
        m.destroy()
    for l in block["ModifiersLabel"]:
        l.destroy()
    block["ModifiersDropDown"] = []
    block["ModifiersLabel"] = []
    block["ModifiersStringVar"] = []
    col_val = 3
    for m in asl_encoding[partName].modifiers:
        block["ModifiersLabel"].append( tkinter.Label( block["entry"], bg=bgColor, text=m.name ) )
        block["ModifiersLabel"][-1].grid( row = 0, column = col_val )
        block["ModifiersStringVar"].append( tkinter.StringVar() )
        block["ModifiersStringVar"][-1].set( m.values[0] )
        block["ModifiersDropDown"].append(tkinter.OptionMenu( block["entry"], block["ModifiersStringVar"][-1], *m.values, command=render ))
        block["ModifiersDropDown"][-1].grid( row = 0, column = col_val+1 )
        col_val += 2
    
    tkinter.Label( block["entry"], text=" ", bg=bgColor ).grid( row = 0, column = 1 )
    tkinter.Button( block["entry"], text="-", command=lambda : removeBlock(index) ).grid( row = 0, column = 0 )

        
    top.buildingBlocks[index] = block
    render(None)


def render(event=None):
    buildString = ""
    pCount = len(top.buildingBlocks)-1

    # build binary string for each part
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
        buildString += " "

    # Update the binary Text Field
    binaryField.config( state = tkinter.NORMAL )
    binaryField.delete( "1.0", tkinter.END )
    binaryField.insert( "1.0", buildString )
    binaryField.config( state = tkinter.DISABLED )


    # Setup lock
    start = time.clock()
    lock = open('tmp/.lock', 'w')
    if (os.path.exists("tmp/.lock")):
        print("LOCK CREATED")
    lock.close()

    # Render Picture
    if sys.version_info.major >= 3:
        blender_process.stdin.write(bytes(buildString+"\n", "UTF-8"))
    else:
        blender_process.stdin.write(buildString+"\n")
    blender_process.stdin.flush()

    # Wait for lock to be deleted by subprocess
    while (os.path.exists("tmp/.lock") and ((time.clock()-start) < 10.0)):
        pass
    if (time.clock()-start) < 10.0:
        print("LOCK WAS REMOVED")

    if ( os.name == "nt" ): #WINDOWS SYSTEM
        #subprocess.call("asl_render.bat")
        subprocess.call("asl_convert.bat")

    elif ( os.name == "posix" ): #MACOSX/LINUX/CYGWIN
        pass

    render = tkinter.PhotoImage(file="tmp\\asl0000.gif")
    renderLabel.render = render
    renderLabel.config( image=render )


newBlock()

addButton = tkinter.Button( selectFrame, text="+", command=newBlock )
addButton.pack( side = tkinter.BOTTOM )


top.mainloop()
