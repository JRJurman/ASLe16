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

trackingModifier = [
]

pivotModifiers = [
    ModifierBlock("wiggle", 2, ["none", "with-the-joint", "against-the-joint"])
]

ballModifiers = [
    ModifierBlock("wiggle",  2, ["none", "x", "y", "z"]),
]

asl_encoding = [
    PartBlock("Face", "0000000", *faceModifiers)
]
