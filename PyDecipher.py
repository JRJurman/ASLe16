"""
Python application that takes in a list of bits and
returns the pose representations
"""

import re           # regex library

class PyDecipher:

    def __init__(self, encoding):
        self.code = dict()
        for e in encoding:
            self.code[e.identifier] = e

    # Convert binary string to english descriptors
    def decipher(self, string):
        part = False
        res = ""
        cPart = None
        for binaryStr in string.split(" "):
            part = not part
            if part:
                res += "Part: "
                cPart = None
                partKey = binaryStr[1:]
                if partKey in self.code.keys():
                    res += self.code[partKey].name + "\n"
                    cPart = partKey
                else:
                    res += "unknown \n"
            else:
                if cPart != None:
                    code = binaryStr
                    for m in self.code[cPart].modifiers:
                        res += "| {}: ".format(m.name)
                        if code[:m.size] in m.values.keys():
                            res += m.values[code[:m.size]] + "\n"
                        else:
                            res += "unknown \n"
                        code = code[m.size:]
        if not self.isValid(string):
            if self.isMissingBits(string):
                res += "err: string is not complete\n"
            if self.isMissingBytes(string):
                res += "err: string has no ending byte\n"
            if self.tooManyBytes(string):
                res += "err: string has an extra byte\n"

        return res



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

