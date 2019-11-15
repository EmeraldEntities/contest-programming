import sys

def read():
    return sys.stdin.readline().rstrip()

endingPoint = read()
slides = [[] for x in range(int(endingPoint))]

while True:
    destination = read().split(" ")

    if destination[0] == "0" and destination[1] == "0":
        break

    slides[int(destination[0]) - 1].append(destination[1])

nodesToTravel = []
confirmedSlides = []
totalPaths = 0 

for start in range(len(slides[0])):
    nodesToTravel.append(slides[0][start])

while len(nodesToTravel) > 0:
    currentNode = nodesToTravel.pop()

    if currentNode == endingPoint:
        totalPaths += 1
    else:
        for start in range(len(slides[int(currentNode) - 1])):
            if slides[int(currentNode) - 1][start] == endingPoint:
                totalPaths += 1
            else:
                nodesToTravel.append(slides[int(currentNode) - 1][start])

sys.stdout.write(str(totalPaths))

#this program TLEs but I just use this one to test and make sure it works
#notes: dmojccc07s4DP is the correct file that works without TLE-ing