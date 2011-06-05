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