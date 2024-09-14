# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Pieutility",
    "author": "Sabbir",
    "description": "Add some utility to pie menu",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D > Add > Mesh > New Object",
    "warning": "",
    "category": "Generic",
}


import bpy
from bpy.types import Menu, Operator

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)

class myBevel(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "my.bevel"
    bl_label = "Object Bevel"

    def execute(self, context):
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].width = 0.15
        bpy.context.object.modifiers["Bevel"].segments = 16
        return {'FINISHED'}

class mySmooth(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "my.smooth"
    bl_label = "Smooth the object"
    
    
    def execute(self, context):
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        return {'FINISHED'}
    

class VIEW3D_MT_PIE_template(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Smooth Addon"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        # pie.operator_enum("mesh.select_mode", "type")
        pie.operator("my.bevel")
        pie.operator("my.smooth")

def register():
    bpy.utils.register_class(VIEW3D_MT_PIE_template)
    bpy.utils.register_class(myBevel) # Now you can run this operator from `python console` using `bpy.ops.my.bevel()`
    bpy.utils.register_class(mySmooth) # Now you can run this operator from `python console` using `bpy.ops.my.smooth()`



def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_template)
    bpy.utils.unregister_class(myBevel)
    bpy.utils.unregister_class(mySmooth)


if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_template")
