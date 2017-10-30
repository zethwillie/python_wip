import maya.cmds as cmds
import zTools.rig.zbw_rig as rig

sel = cmds.ls(sl=True, fl=True)
poss = []
for x in sel:
    y = cmds.pointPosition(x)
    poss.append(y)


pos = rig.average_vectors(poss)

jnt = cmds.joint(name="joint1")
cmds.xform(jnt, ws=True, t=pos)
cmds.parent(jnt, w=True)

# need to figure out how to orient the joint to the verts? 