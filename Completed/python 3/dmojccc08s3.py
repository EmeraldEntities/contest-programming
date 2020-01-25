import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def write(strThing):
    sys.stdout.write(strThing + "\n")

def bfsSearch():
  queue = deque()
  visited = deepcopy(grid)
  queue.append([1, 0, 0])

  found = False
  while len(queue) > 0:
    i = queue.popleft()

    if i[1] == rows - 1 and i[2] == cols - 1:
      write(str(i[0]))
      found = True
      break
    if visited[i[1]][i[2]] == "+": #just to check every direction and to make sure it doesn't go out of bounds
      directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
      for j in directions:
        if i[1] + j[0] >= 0 and i[1] + j[0] < rows and i[2] + j[1] >= 0 and i[2] + j[1] < cols:
          if not ((visited[i[1] + j[0]][i[2] + j[1]] == "x") or (visited[i[1] + j[0]][i[2] + j[1]] == "*")):
            queue.append([i[0] + 1, i[1] + j[0], i[2] + j[1]])
    elif visited[i[1]][i[2]] == "-":
      directions = [[0, -1], [0, 1]]
      for j in directions:
        if i[2] + j[1] >= 0 and i[2] + j[1] < cols:
          if not ((visited[i[1] + j[0]][i[2] + j[1]] == "x") or (visited[i[1] + j[0]][i[2] + j[1]] == "*")):
            queue.append([i[0] + 1, i[1] + j[0], i[2] + j[1]])
    elif visited[i[1]][i[2]] == "|":
      directions = [[1, 0], [-1, 0]]
      for j in directions:
        if i[1] + j[0] >= 0 and i[1] + j[0] < rows:
          if not ((visited[i[1] + j[0]][i[2] + j[1]] == "x") or (visited[i[1] + j[0]][i[2] + j[1]] == "*")):
            queue.append([i[0] + 1, i[1] + j[0], i[2] + j[1]])
    
    visited[i[1]][i[2]] = "x"

  if not found:
    write("-1")

for testcase in range(int(input().rstrip())):
  rows = int(input().rstrip())
  cols = int(input().rstrip())
  grid = [["*" for y in range(cols)] for x in range(rows)]

  for x in range(rows):
    nextLine = input().rstrip()
    for y in range(cols):
      grid[x][y] = nextLine[y]

  bfsSearch()

# completed 1/25/2020
# notes: i was kinda surprised that my bfs worked first try with not much hassle
#        mom are you proud now