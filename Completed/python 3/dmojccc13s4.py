import sys, collections

def read():
    return sys.stdin.readline().rstrip()

def write(thing):
    sys.stdout.write(thing)

################################

people, comparisons = list(map(int, read().split(" ")))

classroom = [[] for x in range(people + 1)]
visited = [False for x in range(people + 1)]

for _ in range(comparisons):
    comparison = list(map(int, read().split(" ")))

    classroom[comparison[0]].append(comparison[1])

toCompare = list(map(int, read().split(" ")))

def recurseCompare(start, destination):
    haveToCompare = collections.deque()
    haveToCompare.append(start)

    found = False
    while len(haveToCompare) > 0 and not found:
        person = haveToCompare.popleft()
        if person == destination:
            found = True

        else:    
            neighbors = classroom[person]

            for kid in range(len(neighbors)):
                if not visited[neighbors[kid]]:
                    visited[neighbors[kid]] = True
                    haveToCompare.append(neighbors[kid])
    
    return found
        
if recurseCompare(toCompare[0], toCompare[1]):
    write("yes")
elif recurseCompare(toCompare[1], toCompare[0]):
    write("no")
else:
    write("unknown")

#completed 11/15/2019
#notes: BFS actually works better than DFS for this problem... Maybe I'll try to do this question again with C++ next time