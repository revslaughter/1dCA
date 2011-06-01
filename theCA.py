# -*- coding: utf-8 -*-
# So what I want to do here is have a string of 1's and 0's in, set the rule you want in, then
# get the generations in, then get the output out.
# 
# I'll work on getting the output in text first, then I'll make a qt4 version
# which should be the real challenge.
#
# I need to make a rule class with a dictionary of possible binary combinations in the rule class
# that uses the number here to determine the...rule that we use.
#

import random

# ruleMake takes an int, r, and returns a string of length 8 and fills in preceding zeroes
# so, rulemake(4) gives you '00000100' and rulemake(42) gives us '00101010' but out of bounds
# rules are caught, returning '00000000' by default.


def ruleMake(r):
  if r in range(0, 256):
    raw = bin(r)[2:]
    zerosToAdd = (8 - len(raw))
    extraZeros = ""
    while zerosToAdd != 0:
      extraZeros += '0'
      zerosToAdd -= 1
    theRuleNo = extraZeros + raw
    return theRuleNo
  else:
    print "Invalid rule! Try something from 0 to 255!"
    return "0" * 8

# What I want to do is when given the rule and a three sequence
# thingy (I'll call it a codon from genetics), whatdo will return the new state.
# For example, if we're given rule 110, whatDo(110, "010") returns "1"
# I'll probably define the dictionary in this function as part of a built in type later on;
# until then, this is probably an inefficient way of doing things. Not as inefficient, though,
# as a bunch of nested 'if' statements, which was my first idea.

def whatDo(rule, codon):
  binaryRule = ruleMake(rule)
  lookItUp = {
    "111" : binaryRule[0],
    "110" : binaryRule[1],
    "101" : binaryRule[2],
    "100" : binaryRule[3],
    "011" : binaryRule[4],
    "010" : binaryRule[5],
    "001" : binaryRule[6],
    "000" : binaryRule[7]
  }
  return lookItUp[codon]

# After thinking about this a little bit, I've come to the conclusion that I must simply
# ignore the ends. That's the only way this can be done the way we're doing it. To ignore
# the ends, I'm just going to copy them from oldState to the ends of newState. Maybe we can
# in the future make this a toroidal map or field, but in the meantime I'll stick with just
# the straight, finite line.

def processTheNext(rule, oldState):
  newState = oldState[0]
  for x in range(1, len(oldState)-1):
    newState += whatDo(rule, oldState[x-1:x+2])
  newState += oldState[-1]
  return newState

# So we're finally to the end game - here's the main algorithm for churning out the stuff
# you tell it what rule to use, what initial binary string to start with, and how many
# iterations or generations to make, with an initial value of 1 if you want to iterate
# using this function without needing to remember 1. It'll still take any value you want
# for the number of generations.
# The default input string is a random 150 bit binary string.

# I've decided to split and replace doTheThing with printTheThing and makeTheThing.
# They take exactly the same arguments, but printTheThing is more about printing it
# and makeTheThing is more about saving and using the output for something else, so
# that you can more easily integrate it in your own programs.

def printTheThing(rule, n=1, initial=bin(random.getrandbits(150))[2:]): 
    output = [initial]
    output += makeTheThing(rule, n, initial)
    printTheMatrix(output)

# printTheMatrix is handy if you've already made a matrix with makeTheThing and just
# want to see how it looks.
def printTheMatrix(a): 
    for x in a:
	print ((x.replace('0', '_')).replace('1', '#') + " " + str(int("0b"+x, 2)))

# So, makeTheThing is just like printTheThing, except for internal use. makeTheThing
# puts each generation in as a list entry, so you may then navigate the output as
# a matrix, so if you put  result = makeTheThing(90, 50, "00000000000000100000000000000")
# you could then treat result as a matrix; result[4][10] == 1.

def makeTheThing(rule, n=1, initial=bin(random.getrandbits(150))[2:]):
    builder = initial
    #output = []
    output.append(builder)
    for x in range(0,n):
	builder = processTheNext(rule, builder)
	output.append(builder)
    return output

#this is just a test value I made.
start = (('0' * 75) + '1' + ('0' * 75))