from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
loadPrcFileData('configurate', 'window-title Loading')
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.showbase import DirectObject
from direct.interval.IntervalGlobal import *
import urllib, os, __main__, random
from pandac.PandaModules import *

import StreetLoader
from panda3d.core import loadPrcFile
from panda3d.core import * 
loadPrcFile("config/config.prc")

#street1 = StreetLoader.loadStreet('20x40')
street1 = StreetLoader.testLoader('20x40')
try:
	street1.place()
	print "placing works"
except:
	print "nonetype bullcrap"

run()
