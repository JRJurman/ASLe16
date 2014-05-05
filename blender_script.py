
import bpy
# identifiers 
rig = bpy.data.objects['metarig']
armature = bpy.data.armatures["Armature"]

# neutral pose
bpy.context.scene.objects.active = rig
bpy.ops.object.mode_set(mode='POSE') # change blender context
bpy.ops.pose.select_all(action='DESELECT') # removes all selections
# select hands
for i in range(10):
    rig.pose.bone_groups.active_index = i
    print(i)
    bpy.ops.pose.group_select()
bpy.ops.poselib.apply_pose(pose_index=2)
# wrist turn
bpy.data.armatures["Armature"]["wrist_roll_R"] = -3.0
bpy.data.armatures["Armature"]["wrist_yaw_R"] = -1.0

"""
# modifying part via pose library
##################################################

# thumb L
rig.pose.bone_groups.active_index = 0
bpy.ops.pose.group_select()

# change poses - finger pose - hand close
rig.pose_library = bpy.data.actions['FingerPoses']
bpy.ops.poselib.apply_pose(pose_index=2)

# modifying part via pose library 2
##################################################

# thumb R
rig.pose.bone_groups.active_index = 6 # different hand is 5 above
bpy.ops.pose.group_select()

# change poses = thumb poses - to web 1
rig.pose_library = bpy.data.actions['ThumbPoses']
bpy.ops.poselib.apply_pose(pose_index=0)

# change driver
##################################################

# wrist turn
armature["wrist_roll_R"] = -3.0
"""

# Encoding
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding

pd = PyDecipher(asl_encoding)
def derp(t, s, u):
	print("derp : {} {} {}".format(t, s, u))
def herp(t, s):
	print("herp func : {} {}".format(t,s))
def foo(v):
	print("foo function : {}".format(v))
def bar():
	print("bar function - is normal")
pd.register(foo, "Face", "EyeBrow")
pd.register(bar, "Face", "EyeBrow", "normal")
pd.register(herp, "Face")
pd.register(derp)
pd.callFunctions("00000000 11111111")
pd.callFunctions("00000000 00000000")
pd.callFunctions("00000001 00000000")
