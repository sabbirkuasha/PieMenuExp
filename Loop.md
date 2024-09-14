```py
import bpy
import bpy.types from (Panel, Operator)

from random import randint

bl_info = {
    "name": "Random Object Spawner",
    "author": "Sabbir",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Random Mesh Object Spawner",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

for i in range(100):
    print(f'Rand: {randint(5,20)}')
    randomScale = randint(0,3)
    x = randint(-40,40)
    y = randint(-40,40)
    z = randint(-40,40)
    #print(randint)
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(x, y, z), scale=(randomScale, randomScale, randomScale), rotation=(x,y,z))
#    bpy.ops.object.shade_smooth()


def register():
    pass

def unregister():
    pass
```
