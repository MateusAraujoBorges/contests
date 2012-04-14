#!/usr/bin/python
import sys,string

input = open(sys.argv[1])
nentries = int(input.readline());
keyfrom = ' acbedgfihkjmlonqpsrutwvyxz'
keyto = ' yehosvcdxiulgkbzrntjwfpamq'

table = string.maketrans(keyfrom,keyto)

i = 1
for line in input:
    print "Case #" + str(i) + ": " + string.translate(line,table),
    i = i + 1


