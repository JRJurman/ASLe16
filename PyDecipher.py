"""
Python application that takes in a list of bits and
returns the pose representations
"""

import re           # regex library

class PyDecipher:

    def __init__(self, encoding):
        self.code = dict()
        self.afterRegister = None
        self.beforeRegister = None
        self.functions = dict()
        for e in encoding.values():
            self.code[e.identifier] = e

    # Convert binary string to english descriptors
    # Returns a List of PartHashes including:
    #       Name : PartName
    #       Modifiers : A list of tuples, that are:
    #               (Modifier Name, Modifier Value)
    def decipher(self, string):
        part = False
        res = []
        cPart = None

        # Add appropriate spaces if there are none
        if (string.find(" ") == -1):
            string = " ".join( i for i in re.findall("([01]{,8})",string) if i != "")

        for binaryStr in string.split(" "):
            part = not part
            if part:
                cPart = None
                partKey = binaryStr[1:]
                if partKey in self.code.keys():
                    res.append( {"name":self.code[partKey].name, "modifiers":[]} )
                    cPart = partKey
                else:
                    res.append( {"name":"unknown", "modifiers":[]} )
            else:
                if cPart != None:
                    code = binaryStr
                    for m in self.code[cPart].modifiers:
                        if code[:m.size] in m.lookup.keys():
                            res[len(res)-1]["modifiers"].append( (m.name, m.lookup[code[:m.size]]) )
                        else:
                            res[len(res)-1]["modifiers"].append( (m.name, "unknown") )
                        code = code[m.size:]
        return res


    # afterRegister - function that gets called after every register call
    def setAfterRegister(self, func):
        self.afterRegister = func

    # beforeRegister - function that gets called after before register call
    def setBeforeRegister(self, func):
        self.beforeRegister = func

    # register a function for a given PartName, PartMod, or ModifierValue
    def register(self, func, PartName=None, PartModifier=None, ModifierValue=None):

        if (PartName == None) and (PartModifier == None) and (ModifierValue == None):
            self.functions[()] = lambda pn, pm, mv: func(pn, pm, mv)

        elif (PartModifier == None) and (ModifierValue == None):
            self.functions[(PartName)] = lambda pm, mv: func(pm, mv)

        elif (ModifierValue == None):
            self.functions[(PartName, PartModifier)] = lambda mv: func(mv)

        elif (ModifierValue != None):
            self.functions[(PartName, PartModifier, ModifierValue)] = lambda : func()

    # Calls Registered Functions on PyDecipher Parts
    def callFunctions(self, string):
        for p in self.decipher(string):
            for m in p["modifiers"]:

                valueKey = (p["name"], m[0], m[1])
                modifierKey = (p["name"], m[0])
                partKey = (p["name"])
                noKey = ()

                if self.beforeRegister != None:
                    self.beforeRegister()
                if ( valueKey in self.functions.keys() ):
                    self.functions[valueKey]()
                elif ( modifierKey in self.functions ):
                    self.functions[modifierKey](m[1])
                elif ( partKey in self.functions ):
                    self.functions[partKey](m[0], m[1])
                elif ( noKey in self.functions ):
                    self.functions[noKey](p["name"], m[0], m[1])
                else:
                    # No Key matches current Part-Modifier-Value
                    pass
                if self.afterRegister != None:
                    self.afterRegister()


    # Do we have blocks of 8?
    def isMissingBits(self, string):
        return re.match(r"^([01]{8} )*$", string)==None

    # Do we have an ending block?
    def isMissingBytes(self, string):
        return re.match(r"0[01]{7} [01]{8}$", string)==None

    # Do we have an extra block?
    def tooManyBytes(self, string):
        return re.match(r"0[01]{7} [01]{8} 1[01]{7} [01]{8}$", string)==None

    # All encompasing regex
    def isValid(self, string):
        return re.match(r"^(1[01]{7} [01]{8} )*(0[01]{7} [01]{8})$", string)

