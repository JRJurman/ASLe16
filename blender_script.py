
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

# PART, MODIFIER NAME, VALUE
def leftHandLocation( position ):
	rig.pose.bone_groups.active_index = 11
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['Locations']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		if position == "waist-center":
			armature["target_chest_L"] = 1
			armature["part_location_L"] = 0
		elif position == "forearm":
			armature["target_forearm_L"] = 1
			armature["part_location_L"] = 0
		elif position == "back-of-wrist":
			armature["target_forearm_L"] = 1
			armature["part_location_L"] = 0
		elif position == "inside-of-wrist": # TOOD : get wrist rot / loc
			armature["target_forearm_L"] = 1
			armature["part_location_L"] = 1
		elif position == "hand": # TODO : get hand
			armature["target_forearm_L"] = 1
			armature["part_location_L"] = 1
		elif position == "torso-center":
			armature["target_chest_L"] = 1
			armature["part_location_L"] = 0.5
		elif position == "upper-arm":
			armature["target_upper_arm_L"] = 1
			armature["part_location_L"] = 0.5
		elif position == "elbow":
			armature["target_upper_arm_L"] = 1
			armature["part_location_L"] = 1
		elif position == "manubrium":
			armature["target_chest_L"] = 1
			armature["part_location_L"] = 1
		else:
			print("INVALID VALUE func leftHandLocation")
		
def rightHandLocation( position ):
	rig.pose.bone_groups.active_index = 10
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['Locations']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		if position == "waist-center":
			armature["target_chest_R"] = 1
			armature["part_location_R"] = 0
		elif position == "forearm":
			armature["target_forearm_R"] = 1
			armature["part_location_R"] = 0
		elif position == "back-of-wrist":
			armature["target_forearm_R"] = 1
			armature["part_location_R"] = 0
		elif position == "inside-of-wrist": # TOOD : get wrist rot / loc
			armature["target_forearm_R"] = 1
			armature["part_location_R"] = 1
		elif position == "hand": # TODO : get hand
			armature["target_forearm_R"] = 1
			armature["part_location_R"] = 1
		elif position == "torso-center":
			armature["target_chest_R"] = 1
			armature["part_location_R"] = 0.5
		elif position == "upper-arm":
			armature["target_upper_arm_R"] = 1
			armature["part_location_R"] = 0.5
		elif position == "elbow":
			armature["target_upper_arm_R"] = 1
			armature["part_location_R"] = 1
		elif position == "manubrium":
			armature["target_chest_R"] = 1
			armature["part_location_R"] = 1
		else:
			print("INVALID VALUE func rightHandLocation")
		
def leftHandShape( position ):
	print("func {:s}, {:d}".format(position, rig.pose_library.pose_markers.keys().index( position )))
	for i in range(0,5):
		rig.pose.bone_groups.active_index = i
		bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['HandShapes']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
        	print("INVALID VALUE func leftHandShape: {}".format(position))

def rightHandShape( position ):
	print("func {:s}, {:d}".format(position, rig.pose_library.pose_markers.keys().index( position )))
	for i in range(5,10):
		rig.pose.bone_groups.active_index = i
		bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['HandShapes']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		print("INVALID VALUE func rightHandShape")
		
def leftThumb( bend ):
	rig.pose.bone_groups.active_index = 0
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['ThumbPoses']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	elif position in rig.pose_library.pose_markers.keys():
		rig.pose_library = bpy.data.actions['FingerPoses']
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		print("INVALID VALUE func leftThumb")
		
def rightThumb( bend ):
	rig.pose.bone_groups.active_index = 5
	bpy.ops.pose.group_select()
	rig.pose_library = bpy.data.actions['ThumbPoses']
	if position in rig.pose_library.pose_markers.keys():
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	elif position in rig.pose_library.pose_markers.keys():
		rig.pose_library = bpy.data.actions['FingerPoses']
		bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( position ))
	else:
		print("INVALID VALUE func rightThumb")
		
def leftThumbTarget( value ):
	armature["L_thumb_target"] = True if spread == "yes" else False

def rightThumbTarget( value ):
	armature["R_thumb_target"] = True if spread == "yes" else False

def finger( partName, modifierName, value ):
	# check if we are dealing with a finger
	if partName[5:] in "".join(["Index","Middle","Ring","Pinky"]):
		if modifierName == "Spread":
			pSpreadName = "palm." + {"Index":"01", "Middle":"02", "Ring":"03", "Pinky":"04"}[partName.split("Left")[-1].split("Right")[-1]] + ".L" if "Left" in partName else ".R"
			armature.bones[pSpreadName].select = True if value == "yes" else False
			rig.pose_library = bpy.data.actions['FingerPoses']
			bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( "spread" ))
		if modifierName == "AtTarget":
			pTargetName = "L_" if "Left" in partName else "R_"
			pTargetName += partName.split("Left")[-1].split("Right")[-1].lower() + "_target"
			print(pTargetName)
			armature.bones[pTargetName] = 1 if value == "yes" else 0
		if modifierName == "Bend":
			rig.pose_library = bpy.data.actions['FingerPoses']
			for i in range(1,4):
				pBendName = "f_" + partName.split("Left")[-1].split("Right")[-1].lower() + ".0{}.".format(i) + "L" if "Left" in partName else "R"
				armature.bones[pBendName].select = True
			if value in rig.pose_library.pose_markers.keys():
				bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( value ))
		if modifierName == "KnuckleBend":
			rig.pose_library = bpy.data.actions['FingerPoses']
			for i in range(2,4):
				pBendName = "f_" + partName.split("Left")[-1].split("Right")[-1].lower() + ".0{}.".format(i) + "L" if "Left" in partName else "R"
				armature.bones[pBendName].select = True
			if value == "bent":
				bpy.ops.poselib.apply_pose(pose_index=rig.pose_library.pose_markers.keys().index( value ))

def before():
	bpy.ops.pose.select_all(action='DESELECT') # removes all selections
	
pd.setBeforeRegister(before)
pd.register(leftHandLocation, "LeftHandLocation", "Location")
pd.register(rightHandLocation, "RightHandLocation", "Location")
pd.register(leftHandShape, "LeftHandShape", "Handshape")
pd.register(rightHandShape, "RightHandShape", "Handshape")
pd.register(leftThumb, "LeftThumb", "Bend")
pd.register(rightThumb, "RightThumb", "Bend")
pd.register(leftThumbTarget, "LeftThumb", "AtTarget")
pd.register(rightThumbTarget, "LeftThumb", "AtTarget")
pd.register(finger)

pd.callFunctions(open("tmp/encode.txt").read())
