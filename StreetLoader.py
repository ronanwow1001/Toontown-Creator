from __future__ import with_statement
from direct.actor.Actor import Actor
from panda3d.core import Filename as pfile
from panda3d.core import PandaSystem, TextNode
from datetime import datetime
import direct.directbase.DirectStart
import fnmatch
import difflib
import sys
import os
import re

def loadStreet(street_name):
	street = loader.loadModel('phase_3.5/models/modules/street_modules.bam')
	if street_name == '10x40':
		try:
			street = street.find('**/street_10x40')
			street.reparentTo(render)
			print "loaded 10x40 street"
		except:
				print "couldn't load street"
	if street_name == '20x40':
		try:
			street = street.find('**/street_20x40')
			street.reparentTo(render)
			print "loaded 20x40 street"
		except:
				print "couldn't load street"
	return street
		
def testLoader(street_name):
	street = loader.loadModel('phase_3.5/models/modules/street_modules.bam')
	try:
		street = street.find('**/street_'+ street_name +'')
		print "it worked, rendering"
		street.reparentTo(render)
		print "rendered"
	except: 
		print "didn't work"
	return street
