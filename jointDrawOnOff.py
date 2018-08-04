# joints on
sel = cmds.ls(type="joint")
for jnt in sel:
    cmds.setAttr("{0}.drawStyle".format(jnt), 0)

# joints off
sel = cmds.ls(type="joint")
for jnt in sel:
    cmds.setAttr("{0}.drawStyle".format(jnt), 2)r("{0}.drawStyle".format(jnt), 0)