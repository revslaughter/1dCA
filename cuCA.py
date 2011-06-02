# -*- coding: utf-8 -*-

from theCA import *

#Seth's idea, I think, was to have a feedback loop regarding each rule where 
#the rule's binary form is applied to itself and the next step becomes another
#rule. I think that this is neat but it seems to settle into loops pretty quickly.
#However, in order to help quantify it, I think that this will just take the initial
#rule and not random bits as in the original idea.

#n, by the way, is the number of iterations you want to make, as ever. 
# Oh, and rule 89 makes a neat 3-step pattern. I wonder which other ones do that.
# Rules 1 and 3 are also surprisingly robust; rule 3 has a 4-step pattern!
# Looks like rules 29, 87, and 113 are the source of the loop, if they crop up look out!
# Maybe I can write an algorithm that calculates differences and detects loops.

def sethThing(inputRule, n): #, initial=ruleMake(random.randrange(0,255))):
    feedMyBack=ruleMake(inputRule)
    builder = makeTheThing(inputRule, 1, feedMyBack)
    for n in range(0,n):
	# So this statement says, "At the end of builder, put the first entry of a 
	# makeTheThing in with the number that the last entry of builder, 
	# just iterated once, and as the initial pattern use the last entry of builder."
	builder.append(makeTheThing(int(('0b'+builder[-1]),2), 1, builder[-1])[1])
    return builder
# sethScan reveals that nothing over rule 127 is interesting! Huh!
# the returned list is [1, 3, 5, 11, 13, 19, 23, 27, 29, 31, 33, 37, 39, 43, 49, 55, 57, 
# 65, 67, 71, 73, 75, 79, 81, 83, 87, 89, 91, 95, 101, 105, 109, 113, 115, 117, 123, 125, 127]

def sethScan():
    neatRuleList=[]
    isInteresting = False
    for x in range(0,255):
	subject = sethThing(x, 20)
	for y in range(0,20):
	    if subject[y] == subject[y+1]:
		isInteresting = False
	    else:
		isInteresting = True
	if isInteresting:
	    neatRuleList.append(x)
	isInteresting = False
    return neatRuleList


#OK, so we're gonna have a range from 0 to 256. For that rule, we're gonna just test each rule once.
#somehow in ScanIt we're testing tons of rules. Shouldn't be happening. Rules only need to be tested
#one time. After they've been tested they go to the dictionary with the key, which is how many steps
#it took to find a string from the bottom that matches.

def scanIt():
    ruleDic={}
    for rule in range(0, 256):
	subject = sethThing(rule, 20)
	count = 1
	for x in range(-19, 1): #counting backwards here
	    if 0-x-count > 0:#we don't want to check to see if subject[-1] is the same as subject[-1]
		if subject[-1] != subject[0-x-count]:
		    count += 1 #put the count up 1 if they don't match.
		else:
		    break #stop if they're the same!
	if count in ruleDic:
	    ruleDic[count].append(rule)
	else:
	    ruleDic[count] = [rule]
    return ruleDic
    
#Dude, scanIt() just reveals two types of patterns, only two. We can dig deeper, but I don't think there's
#reason to. Everything that doesn't repeat every time GOES IN 5's. SERIOUSLY, FIVES, GODDAMNIT - SETH THIS
#IS NOT A JOKE. NOTHING IS TRUE, ALL IS PERMITTED. <(k)
#If you can find more, fine - but seems that everything in /group five/ hits
#that same quintity: 13,105,113,29,81. Peace.

def scanNotRepeat():
    ruleDic={}
    for rule in scanIt()[1]:
	subject = sethThing(rule, 40)
	count = 1
	for x in range(0, 40):
	    if x+count < 40:
		if subject[x] != subject[x+count]:
		    count += 1
		else:
		    break #stop if they're the same!
	if count in ruleDic:
	    ruleDic[count].append(rule)
	else:
	    ruleDic[count] = [rule]
    return ruleDic

#RING CA TIME!!!
from wrapCA import *

def sethRing(inputRule, n): #, initial=ruleMake(random.randrange(0,255))):
    feedMyBack=ruleMake(inputRule)
    builder = makeTheRing(inputRule, 1, feedMyBack)
    for n in range(0,n):
	# So this statement says, "At the end of builder, put the first entry of a 
	# makeTheThing in with the number that the last entry of builder, 
	# just iterated once, and as the initial pattern use the last entry of builder."
	builder.append(makeTheRing(int(('0b'+builder[-1]),2), 1, builder[-1])[1])
    return builder
    
def scanItRing():
    ruleDic={}
    for rule in range(0, 256):
	subject = sethRing(rule, 20)
	count = 1
	for x in range(-19, 1): #counting backwards here
	    if 0-x-count > 0:#we don't want to check to see if subject[-1] is the same as subject[-1]
		if subject[-1] != subject[0-x-count]:
		    count += 1 #put the count up 1 if they don't match.
		else:
		    break #stop if they're the same!
	if count in ruleDic:
	    ruleDic[count].append(rule)
	else:
	    ruleDic[count] = [rule]
    return ruleDic

def scanNotRepeatRing():
    ruleDic={}
    for rule in range(0,256):
	subject = sethRing(rule, 40)
	count = 0
	for x in range(0, 40):
	    if x+count < 40:
		if subject[x] != subject[x+count]:
		    count += 1
		else:
		    break #stop if they're the same!
	if count in ruleDic:
	    ruleDic[count].append(rule)
	else:
	    ruleDic[count] = [rule]
    return ruleDic