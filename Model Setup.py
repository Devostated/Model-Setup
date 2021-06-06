bl_info = {
    "name": "Model Setup",
    "author": "Devostated.",
    "version": (0, 1, 0),
    "blender": (2, 91, 0),
    "location": "Operator Search",
    "description": "Setting up models for UE4 usage."
}
import bpy, os

class model_setup(bpy.types.Operator):
    bl_idname = 'model.setup'
    bl_label = "Setup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        for ttt in bpy.data.objects:
            # Arms and Gloves
            if ttt.name.startswith("v_glove") or ttt.name.startswith("v_sleeve") or ttt.name.startswith("v_bare"):
                for bones in bpy.data.armatures[0].bones['v_weapon'].children_recursive:
                    bones.select = True
                bpy.data.armatures[0].bones["v_weapon"].select = True
                bpy.data.armatures[0].bones["v_weapon.Bip01_L_Forearm"].select = False
                bpy.data.armatures[0].bones["v_weapon.Bip01_L_ForeTwist"].select = False
                for bones in bpy.data.armatures[0].bones['v_weapon.Bip01_L_Forearm'].children_recursive:
                    bones.select = False
                bpy.data.armatures[0].bones["v_weapon.Bip01_R_Forearm"].select = False
                bpy.data.armatures[0].bones["v_weapon.Bip01_R_ForeTwist"].select = False
                for bones in bpy.data.armatures[0].bones['v_weapon.Bip01_R_Forearm'].children_recursive:
                    bones.select = False
                for icon in bpy.data.armatures[0].bones:
                    if icon.name.startswith("camera"):
                        icon.select = True
                    else:
                        pass
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.armature.delete()

            else:
                pass


        for root in bpy.data.objects:
            if root.name.endswith("skeleton"):
                root.name = "root"
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}

class setupPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Model Setup"
    bl_label = "Model Setup"

    def draw(self, context):
        self.layout.operator('model.setup')


def register():
    bpy.utils.register_class(model_setup)
    bpy.utils.register_class(setupPanel)

def unregister():
    bpy.utils.unregister_class(model_setup)
    bpy.utils.unregister_class(setupPanel)