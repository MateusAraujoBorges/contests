import sys
from heapq import heappop,heapify

#functions

def prim(graph, nNodes):
    nodeList = [[100000,0,-1] for i in range(0,nNodes)] #(dist,id,prev)
    nodeList[0][0] = 0
    nodes = [] #this one wont be "heapified"
    visitedNodes = [False] * nNodes 
    for i in range(0,nNodes):
        nodeList[i][1] = i
        nodes.append(nodeList[i])

    root = nodes[0] #root of the min. spanning tree

    heapify(nodeList)

    for z in range(0,nNodes):
        #print nodeList
        current = heappop(nodeList)
        #print current
        currentId = current[1]
        visitedNodes[currentId] = True

        for neighbor in graph[currentId]:
            neighborId = neighbor[0]

            if not visitedNodes[neighborId]:
                neighborNode = nodes[neighborId]
                weight = neighbor[1]

                if weight < neighborNode[0]:  
                    neighborNode[0] = weight
                    neighborNode[2] = currentId

        heapify(nodeList)


    edges = []
    for node in nodes:
        edges.append((node[1] + 1,node[2] + 1))

#   print edges
    return edges

#read and print 

c = 1
while True:
    args = sys.stdin.readline().split()
    nNodes = int(args[0])
    nEdges = int(args[1])

    if nNodes == 0: #end of input
        break

    if c > 1:
        print "" #one empty line between test cases

    print "Teste " + str(c) 
    c = c + 1

    graph = [[] for x in range(0,nNodes)]
    
    for i in range(0,nEdges):
        edge = sys.stdin.readline().split()
        pointA = int(edge[0]) - 1
        pointB = int(edge[1]) - 1
        weigth = int(edge[2])
        graph[pointA].append((pointB,weigth))
        graph[pointB].append((pointA,weigth))

    mst = prim(graph,nNodes)

    for edge in mst:
        a = edge[0]
        b = edge[1]

        if a > 0 and b > 0:
            if a < b:
                print str(a) + " " + str(b)
            else:
                print str(b) + " " + str(a)

 
