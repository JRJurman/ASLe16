import bpy
rig = bpy.data.objects['metarig']
# when changing the rig, must change blender context
bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action='DESELECT') # removes all selections
# select hands
for i in range(10):
    rig.pose.bone_groups.active_index = i
    print(i)
    bpy.ops.pose.group_select()