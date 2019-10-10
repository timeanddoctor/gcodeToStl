import numpy as np
import pandas as pd
import meshio
import copy
import bpy
from bpy import context

bl_info = {
    "name": "GCODE Import",
    "category": "Object",
}

scene = context.scene
cursor = scene.cursor.location
obj = context.active_object
obj_new = obj.copy()
scene.collection.objects.link(obj_new)
obj_new.location = cursor

def register():
    bpy.utils.register_class(ObjectCursorArray)


def unregister():
    bpy.utils.unregister_class(ObjectCursorArray)

if __name__ == "__main__":
    register()
