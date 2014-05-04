import bpy
rig = bpy.data.objects['metarig']
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

