# -*- coding: utf-8 -*-

# class elem is a matrix of lists of 1s and 0s with methods in it?

class elem:
    def __init__(self, rule, gen, initial, isring):
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
	builder = ""
	for x in range(0, len(self.matrix)):
	    for y in self.matrix[x]:
		if y:
		    builder += "#"
		else:
		    builder += "_"
	    builder += "\n"
	return builder
    def ruleform(self, rule):
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
    def nextline(self, binrule, line):
	newline = []
	# I wanted to use lists of the form [1,1,1] but guess what, they're not
	# to be used as dictionary keys. Mutable. I could use tuples, perhaps for
	# clarity but this works too - just use the base-10 version of the codon
	whatdo = {
	    7 : binrule[0],
	    6 : binrule[1],
	    5 : binrule[2],
	    4 : binrule[3],
	    3 : binrule[4],
	    2 : binrule[5],
	    1 : binrule[6],
	    0 : binrule[7]
	}
	newline.append(line[0]) #The ends never change
	for x in range(1, len(line)-1):
	    newline.append(whatdo[((4*line[x-1])+(2*line[x])+(line[x+1]))])
	newline.append(line[-1])
	return newline

    