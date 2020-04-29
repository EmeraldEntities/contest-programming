import sys, math, collections
input = sys.stdin.readline
rows = int(input().rstrip())
cols = int(input().rstrip())

def main():
  grid = []
  visited = {}

  for _ in range(rows):
    grid.append(list(map(int, input().rstrip().split(" "))))

  queue = collections.deque()
  routes = findNumbers(grid[0][0])
  for route in routes:
    if visited.get((route[0], route[1])) != True:
      queue.append(route)
      visited[(route[0], route[1])] = True

  broke = False
  while len(queue) > 0:
    square = queue.popleft()

    if(square[0]+1 == cols and square[1]+1 == rows):
      broke = True
      sys.stdout.write("yes\n")
      break
    
    possibleLocations = findNumbers(grid[square[1]][square[0]])

    for item in possibleLocations:
      if item[0]+1 == cols and item[1]+1 == rows:
        broke = True
        sys.stdout.write("yes\n")
        break

      if visited.get((item[0], item[1])) != True:
        queue.append(item)
        visited[(item[0], item[1])] = True
    if broke:
      break

  if not broke:
    sys.stdout.write("no")
           
def findNumbers(num):
  hpos = set()

  for x in range(math.floor(math.sqrt(num))):
    num1 = num/(x+1)
    if (int(num1) == num1):
      if (num1 - 1 < rows and x < cols and num1 - 1 >= 0):
        hpos.add((x, int(num1-1)))
      if (num1 - 1 < cols and x < rows and num1 - 1 >= 0):
        hpos.add((int(num1-1), x))
  return hpos

main()

#13/15 - TLE'd on the third last case :(