from Encoding import PartBlock, ModifierBlock

# Binary - Number of Values
# 1 - Two Values
# 2 - Four Values
# 3 - Eight Values
# 4 - Sixteen Values
# 5 - Thirty Two Values

faceModifiers = [
    ModifierBlock("EyePosX", 3, 
        ["center", "focus", "left", "right", "farLeft", "farRight"]),
    ModifierBlock("EyePosY", 2, ["center", "focus", "down", "up"]),
    ModifierBlock("Cheek",   1, ["normal", "out"]),
    ModifierBlock("EyeBrow", 2, ["normal", "raised", "together"])
]

fingerModifiers = [
    ModifierBlock("Wiggle", 2, ["none", "with-the-joint", "against-the-joint"]),
    ModifierBlock("Bend",   2, ["open", "half", "closed"]),
    ModifierBlock("knuckleBend", 1, ["open", "bent"])
]

thumbModifiers = [
    ModifierBlock("Wiggle", 2, ["none", "with-the-joint", "against-the-joint"]),
    ModifierBlock("Bend",   2, ["open", "half", "closed", "to-finger"]),
    ModifierBlock("WithIndex", 1, ["no", "yes"]),
    ModifierBlock("WithMiddle", 1, ["no", "yes"]),
    ModifierBlock("WithRing", 1, ["no", "yes"]),
    ModifierBlock("WithPinky", 1, ["no", "yes"]),
]

ballModifiers = [
    ModifierBlock("wiggle",  2, ["none", "yaw", "pitch", "roll"]),
]

asl_encoding = []

key = lambda x:"0"*(7-len(bin(x)[2:])) + bin(x)[2:]
counter = 0
for p in [ ("Face", faceModifiers),
           ("ThumbL", thumbModifiers),
           ("ThumbR", thumbModifiers),
           ("IndexL", fingerModifiers),
           ("IndexR", fingerModifiers),
           ("MiddleR", fingerModifiers),
           ("MiddleL", fingerModifiers),
           ("RingR", fingerModifiers),
           ("RingL", fingerModifiers),
           ("PinkyR", fingerModifiers),
           ("PinkyL", fingerModifiers)
           ]:
    asl_encoding.append( PartBlock(p[0], key(counter), *p[1]) )
    counter += 1
