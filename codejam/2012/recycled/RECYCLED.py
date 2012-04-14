#!/usr/bin/python
import sys,string,math

input = open(sys.argv[1])
nentries = int (input.readline())

def shift(n,pos,nplaces):
    if pos <= 0:
        return n
    else:
        mod = int(math.pow(10,pos))
        newstart = n % mod
        newend = n / mod
        result = (newstart * (math.pow(10,nplaces - pos))) + newend
        return int(result)

def compute(lo,hi):
    nplaces = int(math.log10(lo)) + 1
    interval = range(lo,hi)
    total = 0

    for n in interval:
        found = set()
        for tomove in range(1,nplaces):
            shifted = shift(n,tomove,nplaces)
            if(shifted <= hi and shifted > lo and shifted > n):
#               print "current:{0} - shifted:{1}".format(n,shifted)
                if shifted not in found:
                    found.add(shifted)
                    total = total + 1

#    print "len:" + str(len(a))
    return total

def sliceInterval(lo,hi):
    nplaces_lo = int(math.log10(lo)) + 1
    nplaces_hi = int(math.log10(hi)) + 1
    intervals = []
    
    if nplaces_lo == nplaces_hi:
        intervals.append((lo,hi))
    else:
        factor = math.pow(10,nplaces_lo - 1)
        
        for i in range(nplaces_lo,nplaces_hi + 1):
            interval = ()
            if i == nplaces_lo:
                interval = (lo,(factor * 10) - 1)
            elif i < nplaces_hi:
                interval = (factor,factor * 10 - 1)
            else:
                interval = (factor,hi)
            
            factor = factor * 10
            intervals.append(interval)
    
    return intervals
            

i = 1
for line in input:
    entry = line.split()
    lower = int(entry[0])
    upper = int(entry[1])
    
    intervals = sliceInterval(lower,upper)
    
    total = 0
    for interval in intervals:
        recycled =  compute(int(interval[0]),int(interval[1]))
#        print "total for interval:" + str(interval) + " is " + str(recycled)
        total = total + recycled
    
    print "Case #" + str(i) + ": " + str(total)
    i = i + 1
