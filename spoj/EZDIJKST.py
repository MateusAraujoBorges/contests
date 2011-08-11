import sys
from heapq import heappop,heapify

#functions

def dijkstra(graph,nNodes,start,target):
    nodeList = [[100000,0,-1] for i in range(0,nNodes)] #(dist,id,prev)
    nodeList[start][0] = 0
    nodes = [] #this one wont be "heapified"
    for i in range(0,len(nodeList)):
        nodeList[i][1] = i
        nodes.append(nodeList[i])

    targetNode = nodeList[target] #keep this reference
    heapify(nodeList)

    for z in range(0,nNodes):
        #print nodeList
        current = heappop(nodeList)
        #print current
        currentId = current[1]
        
        if current[0] == 100000: #no more accessible nodes from the source
            break
        else:
            for neighbor in graph[current[1]]:
                #print neighbor
                altDist = current[0] + neighbor[1]
                #print altDist
                nNode = nodes[neighbor[0]] #neighbor node
                #print nNode
                if altDist < nNode[0]: #relax
                    nNode[0] = altDist
                    nNode[2] = currentId
            
            heapify(nodeList)

        if currentId == target:
            break

    return targetNode[0]

#read and print

nCases = int(sys.stdin.readline().split()[0])

for c in range(0,nCases):
    args = sys.stdin.readline().split()
    nNodes = int(args[0])
    nEdges = int(args[1])

    graph = [[] for x in range(0,nNodes)]
    
    for i in range(0,nEdges):
        edge = sys.stdin.readline().split()
        origin = int(edge[0]) - 1
        destiny = int(edge[1]) - 1
        weigth = int(edge[2])
        graph[origin].append((destiny,weigth))

    target = sys.stdin.readline().split()
    start = int(target[0]) - 1
    end = int(target[1]) -1

    pathWeigth = dijkstra(graph,nNodes,start,end)
    if pathWeigth < 100000: #target was reached
        print pathWeigth
    else:
        print "NO"

    

    


    
