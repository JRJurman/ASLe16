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
    ModifierBlock("Handshape", 8, ['relaxed', '1', '3', 'bent3', '4', '5', 'claw5', '6', '7', '8', 'open8', '9', 'flat9', 'a', 'openA', 'b', 'bentB', 'flatB', 'openB', 'c', 'flatC', 'smallC', 'e', 'g', 'h', 'i', 'k', 'l', 'm', 'openM', 'n', 'openN', 'o', 'openO', 'smallO', 'r', 't', 'v', 'bentV', 'x', 'openX', 'y', 'ily', 'corna'])
]

handLocationModifiers = [
    ModifierBlock("Location", 8, [
        "neutral-space", "center-space", "right-space", "left-space", "target",
		"hand", "forehead/brow", "mouth/chin", "eyes/nose", 
        "left-temple", "right-temple", "left-cheek/ear", "right-cheek/ear",  
        "face/head", "shoulder-left", "manubrium", "shoulder-right",
        "torso-left", "torso-center", "torso-right",
        "waist-left", "waist-center", "waist-right",
        "upper-arm", "elbow", "forearm", "back-of-wrist", "inside-of-wrist",
		"up", "down", "forward", "back", "left", "right"])
]

targetModifiers = [
    ModifierBlock("Finger", 8, ["none", "thumb", "index", "middle", "ring", "pinky"])
]

wristModifiers = [
	ModifierBlock("Roll", 4, ["0","1","2","3","-3","-2","-1"]),
	ModifierBlock("Pitch", 2, ["none","toward","tilted","away"]),
	ModifierBlock("Yaw", 2, ["none","toward","tilted","away"])
]



asl_encoding = {}
class ASL_PART: pass

key = lambda x:"0"*(7-len(bin(x)[2:])) + bin(x)[2:]
counter = 0
parts = []
parts.append( ("Face", faceModifiers) )
for p in [
            ("TargetModifiers", targetModifiers),
            ("HandLocation", handLocationModifiers),
            ("HandShape", handShapeModifiers),
			("Wrist", wristModifiers)
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
        print( "\n{} ________ > {}".format(part.identifier, part.name) )
        cursor = 0
        for m in part.modifiers:
            for v in list(m.values):
                binary = "{} {}{}{}".format(part.identifier, "_"*cursor, m.reverseLookup[v], "_"*(8-cursor-m.size))
                print( "{} >   {} : {}".format(binary,  m.name, v) )

            cursor += m.size
