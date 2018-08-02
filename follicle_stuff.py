import zTools.rig.zbw_rig as rig
reload(rig)


# spread the follicles

num =  3.0 # number of folls
double = 2.0*num # number of half steps (to find middle of 'faces')
unit = 1.0/double #each half step distance

nurbs = cmds.ls(sl=True)[0]
shape = cmds.listRelatives(nurbs, s=True)[0]

for x in range(1, int(double), 2): #start at first half step and jump full steps from there
    value = x*unit
    # create a follicle and place here
    rig.follicle(nurbs, name="follicle", v=value)
    
    
# keep follicle joints aligned with general rig alignment
for x in (cmds.ls(sl=True)):
    pos = cmds.xform(x, ws=True, q=True, rp=True)
    cmds.select(cl=True)
    jnt = cmds.joint(name="{0}_JNT".format(x))
    cmds.xform(jnt, ws=True, t=pos)
    
# increment numbers better