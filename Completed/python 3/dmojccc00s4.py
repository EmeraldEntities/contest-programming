import sys, collections

def read():
    return sys.stdin.readline().rstrip()

def write(thing):
    return sys.stdout.write(thing)

distance = int(read())

clubs = []

for club in range(int(read())):
    clubs.append(int(read()))

betterClubs = sorted(clubs, reverse = True)

def BFSFind(distance):
    bestLocations = {}
    queue = collections.deque()
    queue.append([0, 0])

    while len(queue) > 0:
        currentClub = queue.popleft()
        numOfClubs = currentClub[0]
        currentDistance = currentClub[1]

        if currentDistance == distance:
            return numOfClubs

        if (distance - currentDistance) in bestLocations:
            return numOfClubs + bestLocations[distance - currentDistance] + 1

        for club in betterClubs:
            if currentDistance + club <= distance:
                if currentDistance + club not in bestLocations:
                    bestLocations[currentDistance + club] = numOfClubs

                    queue.append([numOfClubs + 1, currentDistance + club])
                
    return -1

minClubs = BFSFind(distance)

message = "Roberta acknowledges defeat." if minClubs == -1 else f"Roberta wins in {minClubs} strokes."
write(message)

#completed 11/20/2019
#notes: the DP was pretty tricky to figure out, but I got it in the end!