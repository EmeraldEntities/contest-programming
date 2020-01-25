import sys

input = sys.stdin.readline

gates = [True for x in range(int(input().rstrip()))]

total = 0
totalPlanes = int(input().rstrip())
for plane in range(totalPlanes):
  index = int(input().rstrip()) - 1
  found = False

  while index > -1:
    if (gates[index]):
      total += 1
      gates[index] = False
      found = True
      break
    else:
      index -= 1
  
  if not found:
    break

sys.stdout.write(str(total))

# not fast enough, idk why