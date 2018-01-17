# backfilling

import fnmatch

a = ["cat", "cat1", "cat2", "cat3", "cat5"]
x = "cat"

outName = None
matches = fnmatch.filter(a, "{0}*".format(x))
lastNums = [y.strip(x) for y in matches]
newNum = None

if not lastNums[0]:
    lastNums[0] = "0"

if len(lastNums) > 1:    
    for d in range(len(lastNums)-1):
        if int(lastNums[d]) + 1 != int(lastNums[d+1]):
            newNum = int(lastNums[d])+1
else:
    newNum = 1

outName = x + str(newNum)
print outName


# no backfilling
import fnmatch

a = ["cat", "cat1", "cat2", "cat33"]

x = "cat"

outName = None

matches = fnmatch.filter(a, "{0}*".format(x))
if matches:
    lastNum = matches[-1].strip(x)
    
    if lastNum:
        lastInt = int(lastNum)
        newNum = lastInt + 1
        outName = x + str(newNum)
    else:
        outName = x + "1"
else:
    outName = x
    
print outName


# other shit

def getTopNodes(objects = [], *args):
    """
    from given list of objects return a list of the top nodes in DAG hierarchy
    Args:
        objects (list): list of scene objects
    Return:
        list: any top nodes of the given objects 
    """ 
    roots = []
    
    for objs in objects:
        obj = ""
        if cmds.objectType(objs)=="transform":
            obj = cmds.ls(objs, l=True, dag=True)[0]
        if obj:
            root = (obj.split("|")[:2])
        if root:
            if len(root) > 1 and root[1] not in roots:
                roots.append(root[1])

    return(roots)