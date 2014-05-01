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

handShapeModifiers = [
    ModifierBlock("Handshape", 8, [
        "v-handshape", "bent-v", "closed-hand", "flat-hand", "curved-hand",
        "claw-hand", "cocked-index", "open-hand", "1-hand", "bent-hand"])
]

handLocationModifiers = [
    ModifierBlock("Location", 8, [
        "neutral-space", "forehead/brow", "mouth/chin", "eyes/nose", "left/temple",
        "right-temple", "left-cheek/ear", "right-cheek/ear", "face/head", 
        "shoulder-left", "manubrium", "shoulder-right",
        "torso-left", "torso-center", "torso-right",
        "waist-left", "waist-center", "waist-right",
        "upper-arm", "elbow", "forearm", "back-of-wrist", "inside-of-wrist", "hand"])
]

fingerModifiers = [
    ModifierBlock("Wiggle", 2, ["none", "with-the-joint", "against-the-joint"]),
    ModifierBlock("Bend",   2, ["open", "half", "closed", "to-thumb"]),
    ModifierBlock("KnuckleBend", 1, ["open", "bent"])
    ModifierBlock("Spread", 1, ["no", "yes"])
]

thumbModifiers = [
    ModifierBlock("Wiggle", 2, ["none", "with-the-joint", "against-the-joint"]),
    ModifierBlock("Bend",   3, ["open", "half", "closed", "to-finger", "to-palm", "to-web-1", "to-web-2"]),
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
