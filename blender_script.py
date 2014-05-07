
import bpy
# identifiers 
rig = bpy.data.objects['metarig']
armature = bpy.data.armatures["Armature"]

# neutral pose
bpy.context.scene.objects.active = rig
bpy.ops.object.mode_set(mode='POSE') # change blender context
bpy.ops.pose.select_all(action='DESELECT') # removes all selections
"""
# example code
# select hands
for i in range(10):
	rig.pose.bone_groups.active_index = i
	bpy.ops.pose.group_select()
bpy.ops.poselib.apply_pose(pose_index=2)
# wrist turn
armature["Armature"]["wrist_roll_R"] = -3.0
armature["Armature"]["wrist_yaw_R"] = -1.0
"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) ))

# Encoding
from PyDecipher import PyDecipher
from asl_encoding import asl_encoding
pd = PyDecipher(asl_encoding)
undoStack = []

# PART, MODIFIER NAME, VALUE
def leftHandLocation( position, addToUndo=True ):
	rig.pose.bone_groups.active_index = 11
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['Locations']
	positions = ['target_chest_L', 'target_forearm_L', 'target_part_location_L', 'target_upper_arm_L']
	for i in positions:
		armature[i] = 0
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		if position == "waist-center":
			armature["target_chest_L"] = 1
			armature["target_part_location_L"] = 0
		elif position == "forearm":
			armature["target_forearm_L"] = 1
			armature["target_part_location_L"] = 0
		elif position == "back-of-wrist":
			armature["target_forearm_L"] = 1
			armature["target_part_location_L"] = 1
		elif position == "inside-of-wrist": # TOOD : get wrist rot / loc
			armature["target_forearm_L"] = 1
			armature["target_part_location_L"] = 1
		elif position == "hand":
			armature["target_hand_L"] = 1
		elif position == "torso-center":
			armature["target_chest_L"] = 1
			armature["target_part_location_L"] = 0.5
		elif position == "upper-arm":
			armature["target_upper_arm_L"] = 1
			armature["target_part_location_L"] = 0.5
		elif position == "elbow":
			armature["target_upper_arm_L"] = 1
			armature["target_part_location_L"] = 1
		elif position == "manubrium":
			armature["target_chest_L"] = 1
			armature["target_part_location_L"] = 1
		else:
			print("INVALID VALUE func leftHandLocation")
	if addToUndo:
		undoStack.append( lambda : leftHandLocation( "neutral-space", False ) )
		
def rightHandLocation( position, addToUndo=True ):
	rig.pose.bone_groups.active_index = 10
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['Locations']
	positions = ['target_chest_R', 'target_forearm_R', 'target_part_location_R', 'target_upper_arm_R']
	for i in positions:
		armature[i] = 0
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		if position == "waist-center":
			armature["target_chest_R"] = 1
			armature["target_part_location_R"] = 0
		elif position == "forearm":
			armature["target_forearm_R"] = 1
			armature["target_part_location_R"] = 0
		elif position == "back-of-wrist":
			armature["target_forearm_R"] = 1
			armature["target_part_location_R"] = 1
		elif position == "inside-of-wrist": # TOOD : get wrist rot / loc
			armature["target_forearm_R"] = 1
			armature["target_part_location_R"] = 1
		elif position == "hand":
			armature["target_hand_R"] = 1
		elif position == "torso-center":
			armature["target_chest_R"] = 1
			armature["target_part_location_R"] = 0.5
		elif position == "upper-arm":
			armature["target_upper_arm_R"] = 1
			armature["target_part_location_R"] = 0.5
		elif position == "elbow":
			armature["target_upper_arm_R"] = 1
			armature["target_part_location_R"] = 1
		elif position == "manubrium":
			armature["target_chest_R"] = 1
			armature["target_part_location_R"] = 1
		else:
			print("INVALID VALUE func rightHandLocation")
	if addToUndo:
		undoStack.append( lambda : rightHandLocation( "neutral-space", False ) )
		
def leftHandShape( position, addToUndo=True ):
	for i in range(0,5):
		rig.pose.bone_groups.active_index = i
		bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['HandShapes']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		print("INVALID VALUE func leftHandShape: {}".format(position))
	if addToUndo:
		undoStack.append( lambda : leftHandShape( "relaxed", False ) )

def rightHandShape( position, addToUndo=True ):
	for i in range(5,10):
		rig.pose.bone_groups.active_index = i
		bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['HandShapes']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		print("INVALID VALUE func rightHandShape")
	if addToUndo:
		undoStack.append( lambda : rightHandShape( "relaxed", False ) )

		
def leftWrist( modifierName, value, addToUndo=True ):
	mod = 0
	if modifierName == "Roll":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_roll_L"] = mod
	if modifierName == "Pitch":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_pitch_L"] = mod
	if modifierName == "Yaw":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_yaw_L"] = mod
	if addToUndo:
		undoStack.append( lambda : leftWrist( modifierName, "none", False ) )

def rightWrist( modifierName, value, addToUndo=True ):
	mod = 0
	if modifierName == "Roll":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_roll_R"] = mod
	if modifierName == "Pitch":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_pitch_R"] = mod
	if modifierName == "Yaw":
		if value == "toward":
			mod = 1
		elif value == "tilted":
			mod = -1
		elif value == "away":
			mod = -2
		armature["wrist_yaw_R"] = mod
	if addToUndo:
		undoStack.append( lambda : rightWrist( modifierName, "none", False ) )
		
def leftTargetModifiers( value, addToUndo=True ):
	for f in ["thumb", "index", "middle", "ring", "pinky"]:
		pTargetName = "L_" + f + "_target"
		armature[pTargetName] = 1 if value == f else 0
	if addToUndo:
		undoStack.append( lambda : leftTargetModifiers( None, False ) )
		
def rightTargetModifiers( value, addToUndo=True ):
	for f in ["thumb", "index", "middle", "ring", "pinky"]:
		pTargetName = "R_" + f + "_target"
		armature[pTargetName] = 1 if value == f else 0
	if addToUndo:
		undoStack.append( lambda : rightTargetModifiers( None, False ) )

def before():	
	bpy.ops.pose.select_all(action='DESELECT') # removes all selections

pd.setBeforeRegister(before)
pd.register(leftHandLocation, "LeftHandLocation", "Location")
pd.register(rightHandLocation, "RightHandLocation", "Location")
pd.register(leftHandShape, "LeftHandShape", "Handshape")
pd.register(rightHandShape, "RightHandShape", "Handshape")
pd.register(leftWrist, "LeftWrist")
pd.register(rightWrist, "RightWrist")
pd.register(leftTargetModifiers, "LeftTargetModifiers", "Finger")
pd.register(rightTargetModifiers, "RightTargetModifiers", "Finger")

bpy.context.scene.render.image_settings.file_format = 'BMP'
frame = bpy.data.scenes["bone+mesh"].frame_current
strFrame = "0"*(4-len(str(frame)))+str(frame)
bpy.data.scenes["bone+mesh"].render.filepath = "./tmp/asl" + strFrame

while True:
	# Grab the next Binary Code
	commIn = input()

	# Calls all the functions for the binary code
	pd.callFunctions(commIn)
	# Tell blender to make a render!
	bpy.ops.render.render( write_still=True )

	# check if lock was created
	if os.path.exists("tmp/.lock"):
		#removing lock
		os.remove("tmp/.lock")
	else:
		print("LOCK NOT FOUND")
        
	# Run the Undo Stack to undo previous poses (in-case they were deleted)
	# This is actually called after so that we don't eat into the render time
	for u in range(len(undoStack)):
		undoStack.pop()()
