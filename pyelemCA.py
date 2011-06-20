# -*- coding: utf-8 -*-

class elem:
"""
The elem class calculates generations of elementary cellular automata using
matrix lists of int type 1s and 0s, stored in the elem.matrix object. 
"""
    def __init__(self, rule, gen, initial, isclosed=1):
	"""
	Initializes to an initial matrix given the number of generations and
	starting position, given as a list of 1s and 0s. 
	
	The default value for whether or not the system is closed (cylindrical) 
	is true, which is how they are normally thought. 
	
	If isclosed is false or 0, then the ends of initial will be repeated.
	
	The dictionary self.whatdo tells us what to do given a position and the given rule.
	"""
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
	"""
	returns a neat pattern of _ and #
	"""
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
	"""
	addgen takes the last position of self.matrix, and calculates the
	next iterations. With this, elem is extensible.
	"""
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
	"""
	Takes an int rule and returns a binary representation,
	in the form of a list. I know that bin() does this, but
	bin() returns a string, which is not useful to this project.
	"""
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
	"""
	nextline is used by addgen and returns the next generation.
	nextline also assumes the 'open' framework that doesn't wrap around.
	"""
	newline = [line[0]] 
	for x in range(1, len(line)-1):
	    newline.append(self.whatdo[(line[x-1], line[x], line[x+1])])
	newline.append(line[-1])
	return newline
    def loopline(self, binrule, line):
	"""
	loopline gives the next generation assuming isclosed=true.
	I think that nextline and loopline should be merged into one method
	that takes into account isclosed.
	"""
	newline = [self.whatdo[(line[-1], line[0], line[1])]]
	for x in range(1, len(line)-1):
	    newline.append(self.whatdo[(line[x-1], line[x], line[x+1])])
	newline.append(self.whatdo[(line[-2], line[-1], line[0])])
	return newline

if __name__=="__main__":
    #This just gives us a test example to make sure that everything
    #is running smoothly. Is everything running smoothly?
    start=([0]*50)+[1]+([0]*50)
    choice = int(raw_input("Rule? "))
    big = elem(choice, 50, start)
    print big