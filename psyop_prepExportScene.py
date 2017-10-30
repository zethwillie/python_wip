import maya.cmds as cmds
    
# will create appropriate groups and move stuff into them for fbx export 

def create_grps(*args):
	"""
	create groups if they don't exist
	"""
	first = True
	found = True
	if not cmds.objExists("geo_Grp"):
		cmds.group(empty=True, n=gGrp)
		cmds.parent(gGrp, "GEO")
	if not cmds.objExists("joint_Grp"):
		cmds.group(empty=True, n=jGrp)
		try:
			cmds.parent(jGrp, "cRoot")
		except:
			first=False
		if not first:
			try:
				cmds.parent(jGrp, "pRoot")
			except:
				cmds.warning("couldn't find pRoot or cRoot")
				found = False
	return(found)
		
def move_geo(*args):
	"""
	move geo to geo grp
	"""
	geo = cmds.ls("*_Geo", type="transform")
	if not geo:
		return()
	cmds.parent(geo, gGrp)
	
def get_jnt_tops(*args):
	"""
	get tops of jnt hierarchies, then calls the move jnts func
	"""    
	jnts = cmds.ls(type='joint')
	rootJnts = []
	if jnts:
		for jnt in jnts:
			parentList = cmds.listRelatives(jnt, ap=True, f=True)
			if parentList:
				pList = parentList[0].split("|")
			jointList = [p for p in pList if p and cmds.nodeType(p) == 'joint']
			rootJnt = jointList[0] if jointList else None
			if rootJnt:
				rootJnts.append(rootJnt)
	move_joints(rootJnts)


def move_joints(rootJnts):
	"""
	moves jnts to grp
	"""
	jntTops = list(set(rootJnts)) 
	for jnt in jntTops:
		cmds.parent(jnt, jGrp)

def process():
	"""
	triggers all the stuff to happen
	"""
	status = create_grps()
	if not status:
		return()
	move_geo()
	get_jnt_tops()
 
jGrp = "joint_Grp"
gGrp = "geo_Grp" 
process()
        