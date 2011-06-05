# -*- coding: utf-8 -*-

# class elem is a matrix of lists with methods it it?
class elem:
    def __init__(rule, gen, initial):
	# For now, just a copy from theCA.py
	builder = initial
	self.matrix = []
	self.matrix.append(builder)
	for x in range(0,n):
	    builder = processTheNext(rule, builder)
	    self.matrix.append(builder)
    def __repr__(self):