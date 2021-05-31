import maya.cmds as cmds
import mel


"""
we're only exporting geo
rigs we may have to do a little more. . . 

what to name exported files?

model check:
    anim curves
    xforms on the geo? is this an issue?
    duplicate names
    deformers?
    display layers?
    any specifics re: names, grouping geo
"""

ngMeshNames = ["pSphe", "pCube", "pCyli", "pCone", "pToru","pPlan", "pPlat"]
meshXforms = [cmds.listRelatives(x, p=True)[0] for x in cmds.ls(type="mesh")]

# get default names
warnNames = []
for y in meshXforms:
    if y[:5] in ngMeshNames:
        ln = cmds.ls(y, l=True)
        warnNames.append(ln)
print "sketchy names: ", warnNames


# check non-manifold

nonManifold = []
for y in meshXforms:
    faces = cmds.ls(y+".f[*]", fl=True)
    cmds.select(faces)
    cmds.polySelectConstraint(m=3, t=8, tp=1)


# non manifold
nonManifold = []
vtx = cmds.ls("mySphere.vtx[*]", fl=True)
cmds.selectType(v=True)
cmds.select(vtx)
cmds.polySelectConstraint(m=3, t=1, nm=True)
bad = cmds.ls(sl=True, fl=True)
print bad

# check for no uvs