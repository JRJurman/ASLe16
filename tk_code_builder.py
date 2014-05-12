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
import subprocess, os, platform

# time library -- make sure that rendering doesn't take forever
import time

# Initialize PyDecipher object
pd = PyDecipher(asl_encoding)

# Colors
fgColor = "navajo white"
buttonColor = "#DFD2B0"
bgColor = "#353535"
detailColor = "DeepSkyBlue4"

# Run tk window
top = tkinter.Tk()
top.title("ASLe16 Interactive Builder")
top.config(bg=bgColor)

# SELECTING FRAME
selectFrame = tkinter.Frame( top, bg=bgColor )
selectFrame.pack( side = tkinter.LEFT, anchor = "nw" )

binaryField = tkinter.Text( selectFrame, fg=fgColor, bg=bgColor, bd=0, state=tkinter.DISABLED, font=(None, 16), height=1, width=17 )
binaryField.pack( side = tkinter.TOP, anchor = "w")

tkinter.Label( selectFrame, bg=bgColor, fg=fgColor, text=("_"*120) ).pack( side = tkinter.TOP )

dropDownFields = tkinter.Frame( selectFrame, bg=bgColor )
dropDownFields.pack( side = tkinter.TOP, anchor = "w" )


# RENDER FRAME
renderFrame = tkinter.Frame( top, bg=bgColor )
renderFrame.pack( side = tkinter.RIGHT )

renderLabel = tkinter.Label( renderFrame, bd=0)
renderLabel.pack()

# FIND PATHS FOR EXTERNAL RESOURCES
# WINDOWS USES IMAGEMAGICK, MAC USES SIPS
blenderPath = ""
convertPath = ""
if platform.system() == "Windows":
    defaultBlenderPath = r"C:\Program Files\Blender Foundation\Blender\blender.exe"   # Default Install Path
    defaultConvertPath = r"C:\Program Files\ImageMagick-6.8.9-q16\convert.exe"
    includedBlenderPath = r"Blender\blender.exe"                                      # Bundled Install Path
    includedConvertPath = r"ImageMagick\convert.exe"
elif platform.system() == "Darwin":
    defaultBlenderPath = r"/Applications/Blender/blender.app/Contents/MacOS/blender"  # Default Install Path
    defaultConvertPath = ""
    includedBlenderPath = r"Blender/blender.app/Contents/MacOS/blender"               # Bundled Install Path
    includedConvertPath = ""
  
if os.path.exists(defaultBlenderPath):
    blenderPath = defaultBlenderPath
elif os.path.exists(includedBlenderPath):
    blenderPath = includedBlenderPath
else:
    blenderPath = tkFileDialog.askopenfile(title="Couldn't Find Blender, Select blender Binary") 
    
if os.path.exists(defaultConvertPath):
    convertPath = defaultConvertPath
elif os.path.exists(includedConvertPath):
    convertPath = includedConvertPath

if platform.system() == "Darwin":
    convertCom = ["sips", "-s", "format", "gif", "tmp/asl0000.bmp", "--out", "tmp/asl0000.gif"]
else:
    if convertPath == "":
        convertPath = tkFileDialog.askopenfile(title="Couldn't Find ImageMagick, Select convert Binary")
    convertCom = [convertPath,"./tmp/asl0000.bmp","./tmp/asl0000.gif"]

blenderCom = [blenderPath,"-b",'ASL_Model.blend',"-P","blender_script.py","-y"]

if os.name == "nt":
    renderCommand = blenderCom
    convertCommand = convertCom
elif os.name == "posix":
    renderCommand = " ".join(blenderCom)
    convertCommand = " ".join(convertCom)

# RENDER DEFAULT IMAGE USING BLENDER EXECUTABLE
print(renderCommand)
blender_process = subprocess.Popen(renderCommand, stdin = subprocess.PIPE, shell=True)

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
    
def removeBlock(block, event=None):

    top.buildingBlocks.remove(block)
    block["entry"].destroy()
    binaryField.config( height = len(top.buildingBlocks) )

    render(None)


def setBlock(index, partName):
    block = top.buildingBlocks[index]

    block["PartStringVar"].set( partName )
    block["PartDropDown"] = tkinter.OptionMenu( block["entry"], block["PartStringVar"], *sorted(asl_encoding.keys()),
                                                command=lambda e: setBlock(index, e))
    block["PartDropDown"].config(bd=0, bg=buttonColor)
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
        block["ModifiersLabel"].append( tkinter.Label( block["entry"], fg=fgColor, bg=bgColor, text=m.name ) )
        block["ModifiersLabel"][-1].grid( row = 0, column = col_val )
        block["ModifiersStringVar"].append( tkinter.StringVar() )
        block["ModifiersStringVar"][-1].set( m.values[0] )
        block["ModifiersDropDown"].append(tkinter.OptionMenu( block["entry"], block["ModifiersStringVar"][-1], *m.values, command=render ))
        block["ModifiersDropDown"][-1].config(bd=0, bg=buttonColor)

        block["ModifiersDropDown"][-1].grid( row = 0, column = col_val+1 )
        col_val += 2
    
    tkinter.Label( block["entry"], text=" ", fg=fgColor, bg=bgColor ).grid( row = 0, column = 1 )
    tkinter.Button( block["entry"], text="-", border=0, command=lambda : removeBlock(block) ).grid( row = 0, column = 0 )

        
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
    if (not os.path.exists("tmp/.lock")):
        print("LOCK WAS NOT CREATED")
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
    if (time.clock()-start) >= 10.0:
        print("LOCK WAS NOT REMOVED")

    subprocess.call(convertCommand, shell=True)

    render = tkinter.PhotoImage(file="tmp/asl0000.gif")
    renderLabel.render = render
    renderLabel.config( image=render )


newBlock()

addButton = tkinter.Button( selectFrame, text="+", border=0, command=newBlock )
addButton.pack( side = tkinter.BOTTOM )
tkinter.Label( selectFrame, bg=bgColor, fg=fgColor, text=("_"*120) ).pack( side = tkinter.BOTTOM )


top.mainloop()
