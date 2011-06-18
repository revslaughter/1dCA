# -*- coding: utf-8 -*-

# class elem is a matrix of lists of 1s and 0s with methods in it?

class elem:
    def __init__(self, rule, gen, initial, isclosed=1):
	self.rule = self.ruleform(rule)
	self.seed = initial
	self.state = isclosed
	self.seed = initial
	self.matrix = [self.seed]
	self.gen = 0
	self.whatdo = {
	    (1,1,1) : self.rule[0],
	    (1,1,0) : self.rule[1],
	    (1,0,1) : self.rule[2],
	    (1,0,0) : self.rule[3],
	    (0,1,1) : self.rule[4],
	    (0,1,0) : self.rule[5],
	    (0,0,1) : self.rule[6],
	    (0,0,0) : self.rule[7]
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
	    newline.append(self.whatdo[(line[x-1], line[x], line[x+1])])
	newline.append(line[-1])
	return newline
    def loopline(self, binrule, line):
	newline = [self.whatdo[(line[-1], line[0], line[1])]]
	for x in range(1, len(line)-1):
	    newline.append(self.whatdo(line[x-1], line[x], line[x+1]))
	newline.append(self.whatdo[(line[-2], line[-1], line[0])])
	return newline

if __name__=="__main__":
    start=[0] * 52
    start.extend([1,0])
    big = elem(110, 50, start, 0)
    print big