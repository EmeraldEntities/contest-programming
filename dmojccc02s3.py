import sys

ROW = 0 
COLUMN = 1

def read():
    return sys.stdin.readline().rstrip("\n")

rows = int(read())
columns = int(read())

backyard = [[True for x in range(columns)]for y in range(rows)]

for each in range(rows):
    row = list(read())
    for index in range(len(row)):
        if index == "X":
            backyard[rows][index] = False

# 4 directions - up, left, right, down

locations = backyard

def isValidSpace(row, column):
    if backyard[row][column]:
        return True
    return False

def move():
    pass

numMoves = int(read())
moves = []
locations = [] # a list of lists

for x in range(numMoves):
    moves.append(read())

for row in backyard:
    for space in row:
        if isValidSpace(row, space):
            currentRow = row
            currentColumn = space
            for direction in moves:
                if direction == "F":
                    pass #move()
                elif direction == "R":
                    pass #turnRight()
                else:
                    pass 

# im just bad at coding 