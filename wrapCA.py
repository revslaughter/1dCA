# -*- coding: utf-8 -*-
from theCA import *

# I just wanted to make a ring-shape way of generating CA instead of the
# line way. Just 'cause, y'know. It's basically the same as makeTheThing.

def makeTheRing(rule, n=1, initial=bin(random.getrandbits(150))[2:]):
    builder = initial
    output = []
    output.append(builder)
    for x in range(0,n):
	builder = processTheRing(rule, builder)
	output.append(builder)
    return output


def processTheRing(rule, oldState):
    start = oldState[-1] + oldState[0] + oldState[1]
    newState = whatDo(rule, start)
    for x in range(1, len(oldState)-1):
	newState += whatDo(rule, oldState[x-1:x+2])
    end = oldState[-2] + oldState[-1] + oldState[0]
    newState += whatDo(rule, end)
    return newState