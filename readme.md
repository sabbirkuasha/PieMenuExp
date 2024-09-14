# Run Custom Add-ons or Script function from blender `python console`

1. Write the operator

   ```py
   class myBevel(bpy.types.Operator):
   """Tooltip"""
   bl_idname = "my.bevel"
   bl_label = "Object Bevel"

   def execute(self, context):
       bpy.ops.object.modifier_add(type='BEVEL')
       bpy.context.object.modifiers["Bevel"].width = 0.15
       bpy.context.object.modifiers["Bevel"].segments = 16
       return {'FINISHED'}
   ```

2. Register & Unregister the operator

   ```py
   def register():
   bpy.utils.register_class(myBevel) # Now you can run this operator from `python console` using `bpy.ops.my.bevel()`

   def unregister():
       bpy.utils.unregister_class(myBevel)
   ```

3. Open `pyhon console` & run
   ```
   bpy.ops.my.bevel
   ```
   > `ops` - because its operator
   > `my.bevel` - is the id name
