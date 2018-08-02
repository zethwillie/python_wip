import maya.cmds as cmds

# select the base jnt first, then all ctrl joints (assumes jnts are parented under ctrls, which are in groups colocated
sel = cmds.ls(sl=True, type="joint")
for i in range(len(sel)):
    sc = cmds.listConnections(sel[i], type="skinCluster")[0] # this . . . we need to get the proper skin cluster (there may be multiple)
    
    mx = cmds.listConnections("{0}.worldMatrix[0]".format(sel[i]), d=True, p=True)[0]
    index = mx.split("[")[1].split("]")[0]
    if i==0:
        cmds.connectAttr("{0}.worldInverseMatrix[0]".format(sel[i]), "{0}.bindPreMatrix[{1}]".format(sc, index), f=True)
    else:
        par = cmds.listRelatives(sel[i], p=True)[0]
        cmds.connectAttr("{0}.parentInverseMatrix[0]".format(par), "{0}.bindPreMatrix[{1}]".format(sc, index), f=True)
