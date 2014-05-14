#ASLe16
__Created By Jesse Jurman and Ethan Jurman__

ASLe16 is an encoding system that represents the American Sign Language using a 16 bit encoding.


## What's Inside the Box!

### asl_encoding.py

To generate a full listing of encodings, run (hint, you may want to append ```| less``` to the call to make it easier to read):

    python asl_encoding.py

Python script; asl_encoding is a script that generates all the binary encodings. The script uses the PartBlock and ModifierBlock classes from Encoding.py, and is loaded into the construction of PyDecipher

### ASL_Model.blend

Binary Blender file; This is the blender armature that has been rigged with various drivers to work with the blender_script.py. If you have Blender installed, you may open the file with that, and can change some render settings (although some are forced in the blender_script.py)

### blender_script.py

This file can be run by itself, and takes binary strings from standard-in. The images rendered will be placed in the ./tmp/ located in this folder.

    python blender_script.py

Python Script; This script works with the ASL_Model.blend file and the bpy library which allows python to interact with blender in a scriptable way. This file also makes use of the PyDecipher class, which allows registering functions to a given decipherment. 

Every function in this file describes how the armature in blender should be modified to make the correct pose. Each function also appends to an ```undoStack``` which is a list of functions which get called after each render is made. The ```undoStack``` is required to put the model in the default pose, ready for the next one.

### Encoding.py

Python Script; This file contains the PartBlock and ModifierBlock classes, which are created by the asl_encoding.py script, and are loaded by the PyDecipher script.

Any PartBlock contains the name for a part, it's binary encoding (in 7-bits) and a list of ModifierBlocks.

Any ModifierBlock contains the name of the modifier, the size the modifier takes in binary, and a list of values (in the order that they should be mapped to). 

### \_\_init\_\_.py

Python Script; Tells python that files located here may be used for other python scripts.

### launcher.bat

Batch Script; Batch file that can be double-clicked in Windows to open the program (literally just opens tk_code_builder.py with python).

### launcher.command

Bash Script; Bash script that can be double-clicked in Mac OS X to open the program (literally just opens tk_code_builder.py with python).

### PyDecipher.py

Python Script; Python script that loads a hash of PartBlocks (it only reads in the values) and can make function calls or print strings based on binary-strings that map to those PartBlocks.

It contains a ```decipher(self, string)``` method, which takes in a string and returns a list of hashes that have Name -> PartBlock.name and Modifiers -> a list of tuples that are: (ModifierName, ModifierValue).

Also included is a list of register functions, including ```setAfterRegister(self, func)```, ```setBeforeRegister(self, func)```, ```register(self, func, PartName=None, PartModifier=None, ModifierValue=None)```, and finally ```callFunctions(self, string)```.
```callFunctions(self, string)``` calls a function set in ```setBeforeRegister(self, func)```, all the functions defined in ```register(self, func, ...)``` in order of least generic to most generic, and a function set in ```setAfterRegister(self, func)```. 
```callFunctions(self, string)``` takes in a binary-string, similar to the ```decipher(self, string)``` function, but instead of returning a hash of PartBlocks, it simply calls the registered functions.

At the very end of the file are several validation methods (all regexes), which check if the encoding is in a valid format: ```isValid(self, string)```, ```isMissingBits(self, string)```, ```isMissingBytes(self,sting)``` and ``tooManyBytes(self, string)```.

### README.md

MarkDown File; This file, a description of each file and folder required for running the application.

### tk_code_builder.py

    python tk_code_builder.py

Graphical User Interface for blend_script.py. This file loads a client window written in Tkinter to allow users to select PartBlocks from the asl_encoding.py and pipe binary strings to the blender_script.py (which runs in a ```subprocess.Popen``` call).
Renders which are placed in the ./tmp/ folder are converted into ```.gif``` files, either with ```sips``` (on mac) or with ```ImageMagick``` (on Windows) and loaded in the right pane.
