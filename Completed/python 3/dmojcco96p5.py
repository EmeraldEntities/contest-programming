import sys, collections

def read():
    return sys.stdin.readline().rstrip()

def write(thing):
    return sys.stdout.write(thing)


cities = {}
starting = list(map(int, read().split(" ")))

for _ in range(starting[0]):
    pair = read().split(" ")
    
    if pair[0] not in cities:
        cities[pair[0]] = []
    if pair[1] not in cities:
        cities[pair[1]] = []

    cities[pair[0]].append(pair[1])
    cities[pair[1]].append(pair[0])

routes = []

def findPath():
    global routes
    queue = collections.deque()
    goal = read().split(" ")
    visited = []

    queue.append([goal[0], goal[0][0]])

    while len(queue) > 0:
        currentCity = queue.popleft()
        if currentCity[0] == goal[1]:
            return currentCity[1]
        
        citiesToGo = cities[currentCity[0]]

        for city in range(len(citiesToGo)):
            if citiesToGo[city] not in visited:
                queue.append([citiesToGo[city], currentCity[1] + citiesToGo[city][0]]) 
                visited.append(citiesToGo[city])

for route in range(starting[1]):
    routes.append(findPath())

for path in routes:
    write(path + "\n")

#completed 11/18/2019
#notes: MLEd the first few times and sadly i lost the race because of this :()