import sys

def read():
    return sys.stdin.readline().rstrip()

endingPoint = int(read())
slides = [[] for x in range(int(endingPoint) + 1)]

while True:
    destination = list(map(int, read().split(" ")))

    if destination[0] == 0 and destination[1] == 0:
        break

    slides[int(destination[0])].append(destination[1])

jumps = [0 for node in range(int(endingPoint) + 1)]

def recurseFind(currentNode):
    global jumps

    if currentNode == endingPoint:
        return 1
        
    neighbors = slides[currentNode]
    totalJumps = 0

    for node in range(len(neighbors)):
        if jumps[neighbors[node]] == 0:
            totalJumps += recurseFind(neighbors[node])
        else:
            totalJumps += jumps[neighbors[node]]
    
    jumps[currentNode] = totalJumps

    return totalJumps

print(recurseFind(1))

#completed 11/15/2019
#notes: mann this one was fun. It was fun trying to figure out the DP involved, but there's probably an algorithm
#       out there somewhere with this structure or similar lol