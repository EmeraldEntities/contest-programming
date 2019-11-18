import sys, collections

directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def read():
    return sys.stdin.readline().rstrip()

def write(strThing):
    sys.stdout.write(strThing)

def initMap():
    dimensions = list(map(int, read().split(" ")))
    locations = [[] for x in range(dimensions[1])]

    for thing in range(dimensions[1]):
        row = read()
        locations[thing] = list(row)

    return locations

def findStart():
    for i in range(len(room)):
        for j in range(len(room)):
            if room[i][j] == "C":
                return [i, j]

def bfsPath(queue, room):
    while len(queue) > 0:
        location = queue.popleft()

        if room[location[0]][location[1]] == "W":
            return location[2]

        room[location[0]][location[1]] = "#"

        for direction in directions:
            if ((location[0] + direction[0] < len(room) and location[0] + direction[0] >= 0) and
                (location[1] + direction[1] < len(room[0]) and location[1] + direction[1] <= 0) and
                room[location[0] + direction[0]][location[1] + direction[1]] != "X" and 
                room[location[0] + direction[0]][location[1] + direction[1]] != "#"):

                queue.append([location[0] + direction[0], location[1] + direction[1], location[2] + 1])

outputs = []

for testcase in range(int(read())):
    paths = collections.deque()

    room = initMap()
    start = findStart()

    paths.append([start[0], start[1], 0])
    minJumps = bfsPath(paths, room)

    output = "#notworth" if minJumps >= 60 else str(minJumps)
    outputs.append(output)

for thing in outputs:
    write(thing)  

#suspended cause of that stupid if loop
#also i didnt check to see if an element is already in the queue
#note to self: do that later