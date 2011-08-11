import sys

args = sys.stdin.readline().split()
nNodes = int(args[0])
nEdges = int(args[1])

graph = [[] for x in range(0,nNodes)]
markedNodes = [False] * nNodes

#functions
def cycleSearch(nodeIndex,origin):
    global markedNodes
#    print nodeIndex
#    print markedNodes
#    print graph
#    print "------------"
    result = False
    for node in graph[nodeIndex]:
        if node == origin: #we dont want to go back where we came from
            continue

        if markedNodes[node]:
            result = True
            break
        else:
            markedNodes[node] = True
            t = cycleSearch(node,nodeIndex)
            if t:
                result = True
                break

    return result

#create graph
result = "YES"

for i in range(0,nEdges):
    edge = sys.stdin.readline().split()
    origin = int(edge[0]) - 1
    destiny = int(edge[1]) - 1
    if origin == destiny: #catch this right at start
        result = "NO"
        break
    else:
        graph[origin].append(destiny)
        graph[destiny].append(origin)


if result == "YES":
    markedNodes[0] = True
    if cycleSearch(0,0): #TODO check if this break with an edge like (1,1)
        result = "NO"
    elif not reduce(lambda a,b: a and b, markedNodes): #check if all nodes were visited
        result = "NO"
    
print result



