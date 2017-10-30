"""
reference and import rigs
make sure you have "geo_Grp", "root_Jnt" in scene (a basic rig structure already)
select top node for each imported rig
this will then:
get children of root jnts of imports- move to under root jnt of orig
get CTRL grp of imports - move contents to CTRL of orig, (you should manually put these under control structure once they're in group)
get all geo & children - move to geo_Grp
Then you should deal with namespaces (just replace ":" with "_" on all nodes, for example, or use the namespace editor) for the unreal export script
"""


import maya.cmds as cmds
# select top grp of new rigs
sel = cmds.ls(sl=True)
if sel:
    for top in sel:
        allChld = cmds.listRelatives(top, ad=True, c=True, type="transform")
        chldGeo = [x for x in allChld if x.rpartition("_")[2]=="Geo"]
        chldRootJnt = [x for x in allChld if x.rpartition(":")[2]=="root_Jnt"][0]
        chldCtrl = [x for x in allChld if x.rpartition(":")[2]=="CTRL"][0]
        chldChldJnts = cmds.listRelatives(chldRootJnt, c=True, type="joint")
        chldChldCtrl = cmds.listRelatives(chldCtrl, c=True, type="transform")
        
        cmds.parent(chldGeo, "geo_Grp")
        for jnt in chldChldJnts:
            cmds.parent(jnt, "root_Jnt")
            
        for ctrl in chldChldCtrl:
            cmds.parent(ctrl, "CTRL")
        