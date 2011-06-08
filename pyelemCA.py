# -*- coding: utf-8 -*-

# class elem is a matrix of lists of 1s and 0s with methods in it?

class elem:
    def __init__(rule, gen=0, initial, isring=False):
	self.rule = self.ruleform(rule)
	self.seed = initial
	self.loop = isring
	builder = initial
	self.matrix = []
	self.matrix.append(builder)
	if self.loop:
	    for x in range(0,gen):
		builder = self.loopline(self.rule, builder)
		self.matrix.append(builder)
	else:
	    for x in range(0,gen):
		builder = self.nextline(self.rule, builder)
		self.matrix.append(builder)
    def __repr__(self):
	for x in self.matrix:
	    #This will have to change based on what we have in self.nextline
	    print ((x.replace('0', '_')).replace('1', '#') + " " + str(int("0b"+x, 2)))
    def ruleform(rule):
	binaryform=[]
	if rule in range(0, 256):
	    quotient = 128
	    while (quotient > 0):
		if rule >= quotient:
		    binaryform.append(1)
		    rule = rule - quotient
		else:
		    binaryform.append(0)
		quotient = quotient/2
	return binaryform
    def nextline(rule, line):
	
    
    