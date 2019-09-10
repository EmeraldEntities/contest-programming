import sys

startPos = list(map(int, sys.stdin.readline().split(" ")))
endPos = list(map(int, sys.stdin.readline().split(" ")))
#A knight can only move 2 then 1
print(startPos, endPos)

NEW_X = 0
NEW_Y = 1

possibleMovesU = [[2, 1], [1, 2], [-2, 1], [-1, 2]]
possibleMovesD = [[2, -1], [1, -2], [-2, -1], [-1, -2]]
possibleMovesR = [[2, 1], [1, 2], [2, -1], [1, -2]]
possibleMovesL = [[-2, 1], [-1, 2], [-2, -1], [-1, -2]]
totalMoves = []
moves = 0

def findRecursiveSolution(startPos, endPos, moves, totalMoves, layer):
    layer += 1
    moves += 1
    if startPos[0] == endPos[0] and startPos[1] == endPos[1]:
        layer -= 1
        return moves - 1
    
    elif (startPos[0] < 1 or startPos[1] < 1) or (startPos[0] > 8 or startPos[1] > 8):
        return 99
        layer -= 1

    else:
        if startPos[0] < endPos[0] amd startPos[1] < endPos:
            pass

    else:
        for moveset in range(len(possibleMoves)):
            print(layer)
            print(findRecursiveSolution([startPos[0] + possibleMoves[moveset][NEW_X], startPos[1] + possibleMoves[moveset][NEW_Y]], endPos, moves, totalMoves, layer))

findRecursiveSolution(startPos, endPos, moves, totalMoves)

print(totalMoves)
    
#suspended cause i can't recursion