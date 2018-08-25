import maya.cmds as cmds
import zTools.rig.zbw_rig as rig

pts = cmds.ls(sl=True, fl=True)
mesh = cmds.ls(*pts, o=True)[0]
# throw error if more than one is selected?
obj = cmds.listRelatives(mesh, p=True)[0]
initPos = rig.average_point_positions(pts)
cpom = rig.closest_point_on_mesh_position(initPos, obj)
crom = rig.closest_point_on_mesh_rotation(initPos, obj)

#create softmod
cmds.select(obj, r=True)
softList = cmds.softMod(relative=False, falloffCenter=cpom, falloffRadius=5.0, n="testSM",
                              frontOfChain=True)
#create both controls
baseCtrl = rig.create_control("base", type="cube")
baseGrp = rig.group_freeze(baseCtrl)
moveCtrl = rig.create_control("move", type="sphere")
moveGrp = rig.group_freeze(moveCtrl)
cmds.parent(moveGrp, baseCtrl)

cmds.xform(baseGrp, ws=True, t=cpom)
cmds.xform(baseGrp, ws=True, ro=crom)

# do mult matrix

# also mult scale by falloff attr to get final falloff
# needs to go front of stack
# how to add to set? cmds.softMod(modName, e=True, geometry=newGeoToAdd) #[remove=geoToRemove]

dm = cmds.shadingNode("decomposeMatrix", asUtility=True, name="test_dm")
cmds.connectAttr("{0}.worldMatrix[0]".format(baseCtrl), "{0}.inputMatrix".format(dm))
cmds.connectAttr("{0}.worldInverseMatrix[0]".format(baseCtrl), "{0}.postMatrix".format(softList[0])) ####
cmds.connectAttr("{0}.worldMatrix[0]".format(baseCtrl), "{0}.preMatrix".format(softList[0])) ######
cmds.connectAttr("{0}.matrix".format(moveCtrl), "{0}.weightedMatrix".format(softList[0]))##
cmds.connectAttr("{0}.outputTranslate".format(dm), "{0}.falloffCenter".format(softList[0]))##
cmds.connectAttr("{0}.worldMatrix[0]".format(moveCtrl), "{0}.matrix".format(softList[0]), f=True)
cmds.setAttr("{0}.v".format(softList[1]), 0)
cmds.parent(softList[1], moveCtrl)