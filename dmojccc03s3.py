import sys

input = sys.stdin.readline

directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

boards = int(input().rstrip())
rows = int(input().rstrip())
cols = int(input().rstrip())

grid = []

for _ in range(rows):
  grid.append(list(input().rstrip()))

boardsNeeded = []

def floodfill(spot):
  spots = []

  grid[spot[1]][spot[0]] = "x"

  for i in range(len(directions)):
    if ((spot[1] + directions[i][0] >= 0 and spot[1] + directions[i][0] < len(grid)) and 
    (spot[0] + directions[i][1] >= 0 and spot[0] + directions[i][1] < len(grid[0]))):
      if grid[spot[1]+directions[i][0]][spot[0]+directions[i][1]] != "x":
        spots.append([spot[0] + directions[i][1], spot[1] + directions[i][0]])

  total = 0

  for i in spots:
    total += floodfill(i)
  
  return 1 + total

sortedBoards = sorted(boardsNeeded, reverse=True)