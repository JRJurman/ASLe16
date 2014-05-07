"""
Classes for PartBlocks, and ModifierBlocks
"""

"""
PartBlock - a description of a Part, contains several ModifierBlocks
"""
class PartBlock:
    """
    create new PartBlock
        name (string) - name of part
        identifier (string) - binary string, 7bit identifier
        *modifiers - ModifierBlocks to be added to part
    """
    def __init__(self, name, identifier, *modifiers):
        self.name = name
        self.identifier = identifier
        self.modifiers = []

        for m in modifiers:
            self.modifiers.append(m)

"""
ModifierBlock - a description of a portion of a Modifier
"""
class ModifierBlock:
    """
    create new ModifierBlock
        name (string) - name of modifier
        size (int) - number of bits to modifier
        values (list) - representations in order
        *values will assign themselves to binary string value at the index
        *['center', 'up', 'down'] => {'00':'center', '01':'up', '10':'down'}
    """
    def __init__(self, name, size, values):
        self.name = name
        self.size = size
        self.values = []
        self.lookup = {}
        self.reverseLookup = {}

        c = 0
        for v in values:
            key = "0"*(size - len(bin(c)[2:])) + bin(c)[2:]
            self.values.append(v)
            self.lookup[key] = v
            self.reverseLookup[v] = key
            c += 1
