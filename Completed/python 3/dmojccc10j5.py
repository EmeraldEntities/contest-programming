import sys, collections

def read():
    return sys.stdin.readline().rstrip()

def recurseKnight(x, y, jumps):
    for i in range(len(directions)):
        if x + directions[i][0] <= 8 and x + directions[i][0] >= 1 and y + directions[i][1] <= 8 and y + directions[i][1] >= 1:
            queue.append([x + directions[i][0], y + directions[i][1], jumps + 1])

queue = collections.deque()
directions = [[2, 1], [1, 2], [-2, 1], [-1, 2], [-2, -1], [-1, -2], [1, -2], [2, -1]]

startPos = read().split(" ")

startY = int(startPos[0])
startX = int(startPos[1])
queue.append([startX, startY, 0])

ending = list(map(int, read().split(" ")))

while True:
    currentAnswer = queue.popleft()
    if currentAnswer[0] == ending[1] and currentAnswer[1] == ending[0]:
        sys.stdout.write(str(currentAnswer[2]))
        break 
    
    recurseKnight(currentAnswer[1], currentAnswer[0], currentAnswer[2])

#completed 11/14/2019
#notes: jeez don't do abs(int(startPos[0]) - 8) that just screws this program up for some reason