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
    ModifierBlock("KnuckleBend", 1, ["open", "bent"]),
    ModifierBlock("Spread", 1, ["no", "yes"]),
    ModifierBlock("AtTarget", 1, ["no", "yes"])
]

thumbModifiers = [
    ModifierBlock("Wiggle", 2, ["none", "with-the-joint", "against-the-joint"]),
    ModifierBlock("Bend",   3, ["open", "half", "closed", "to-finger", "to-palm", "to-web-1", "to-web-2"]),
]

asl_encoding = {}
class ASL_PART: pass

key = lambda x:"0"*(7-len(bin(x)[2:])) + bin(x)[2:]
counter = 0
parts = []
parts.append( ("Face", faceModifiers) )
for p in [
            ("Thumb", thumbModifiers),
            ("Index", fingerModifiers),
            ("Middle", fingerModifiers),
            ("Ring", fingerModifiers),
            ("Pinky", fingerModifiers),
            ("HandLocation", handLocationModifiers),
            ("HandShape", handShapeModifiers)
         ]:
    parts.append( ("Left"+p[0], p[1]) )
    parts.append( ("Right"+p[0], p[1]) )


for p in parts:
    part = PartBlock(p[0], key(counter), *p[1])
    asl_encoding[p[0]] = part
    # sets PartBlock to PARTNAME
    setattr(ASL_PART, p[0].upper(), part)
    counter += 1

if __name__ == '__main__':
    for part in sorted(asl_encoding.values(), key=lambda x: x.name ):
        print( "{}".format(part.name) )
        for m in part.modifiers:
            print( "| {} : {}".format(m.name, list(m.values.values())) )
