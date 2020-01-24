import sys, heapq
input = sys.stdin.readline

numCities = input().rstrip()
allPaths = [[-1, []] for x in numCities]

routes = int(input().rstrip())
for route in range(routes):
    x, y, c = map(int, input().rstrip().split(" "))
    allPaths[x].append([y, c])
    allPaths[y].append([x, c])

startNodes = []
goodCities = int(input().rstrip())

for city in range(goodCities):
    d, p = map(int, input().rstrip().split(" "))
    startNodes.append([d, p])

#dijkstra's time :))

finCity = int(input().rstrip())

for node in startNodes:
    unvisited = []
    for x in allPaths[node]:
        heapq.heappush(unvisited, x[1])

    # priority queue for dijkstra?
    #while len(unvisited) > 0:


#I don't even know if this is possible in python but id like to try