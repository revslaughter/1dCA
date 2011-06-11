# -*- coding: utf-8 -*-

# class elem is a matrix of lists of 1s and 0s with methods in it?

class elem:
    def __init__(self, rule, gen, initial, isclosed=1):
	self.rule = self.ruleform(rule)
	self.seed = initial
	self.state = isclosed
	self.seed = initial
	self.matrix = [self.seed]
	self.gen = gen
	#Dictionary to look up keys for given rule, see self.codon
	self.whatdo = {
	    7 : self.rule[0],
	    6 : self.rule[1],
	    5 : self.rule[2],
	    4 : self.rule[3],
	    3 : self.rule[4],
	    2 : self.rule[5],
	    1 : self.rule[6],
	    0 : self.rule[7]
	}
	self.addgen(gen)
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
    def addgen(self, newgen):
	builder = self.matrix[-1]
	if self.state:
	    for x in range(0,newgen):
		builder = self.loopline(self.rule, builder)
		self.matrix.append(builder)
	else:
	    for x in range(0,newgen):
		builder = self.nextline(self.rule, builder)
		self.matrix.append(builder)
	self.gen += newgen
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
	newline = [line[0]] #The ends never change
	for x in range(1, len(line)-1):
	    newline.append(self.codon(line[x-1], line[x], line[x+1]))
	newline.append(line[-1])
	return newline
    def loopline(self, binrule, line):
	newline = [self.codon(line[-1], line[0], line[1])]
	for x in range(1, len(line)-1):
	    newline.append(self.codon(line[x-1], line[x], line[x+1]))
	newline.append(self.codon(line[-2], line[-1], line[0]))
	return newline
    # translates into a form that whatdo understands
    def codon(self, a, b, c): return self.whatdo[((4*a)+(2*b)+(c))]