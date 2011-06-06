# -*- coding: utf-8 -*-

# class elem is a matrix of lists with methods in it?

class elem:
    def __init__(rule, gen, initial, isring):
	# For now, just a copy from theCA.py
	self.rule = rule
	self.seed = initial
	self.loop = isring
	builder = initial
	self.matrix = []
	self.matrix.append(builder)
	if self.loop:
	    for x in range(0,n):
		builder = self.loopline(rule, builder)
		self.matrix.append(builder)
	else:
	    for x in range(0,n):
		builder = self.nextline(rule, builder)
		self.matrix.append(builder)
    def __repr__(self):
	for x in self.matrix:
	    #This will have to change based on what we have in self.nextline
	    print ((x.replace('0', '_')).replace('1', '#') + " " + str(int("0b"+x, 2)))
    def nextline(rule, line):
	binaryform=[]
	if rule in range(0, 256):
	    