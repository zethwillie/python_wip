import os
import maya.cmds as cmds

# get general maya info (where is the interpreter for this version?)
# set the directory to run the thing in mayapy
# get the current scene info (location, scene name, etc)
# get the current selection of things
# create a little python text that runs background maya, enables python, selects those objects, and exports them as alembics
# button to select where to save to
# small ui
# write out python file? 
# option to write out to file or to just run the background process from there


a = "some text\nSome more text\n"

path = "C:/Users/zeth/Desktop"

with open(os.path.join(path, "myFile.py"), "w") as theFile:
    theFile.write(a)
    
#print cmds.internalVar(upd=True)
