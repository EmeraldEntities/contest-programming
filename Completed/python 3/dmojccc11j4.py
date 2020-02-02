import sys

input = sys.stdin.readline

visited = [[0, -1], 
[0, -2], 
[0, -3], 
[1, -3],
[2, -3],
[3, -3],
[3, -4],
[3, -5],
[4, -5],
[5, -5],
[5, -4],
[5, -3],
[6, -3],
[7, -3],
[7, -4],
[7, -5],
[7, -6],
[7, -7],
[6, -7],
[5, -7],
[4, -7],
[3, -7],
[2, -7],
[1, -7],
[0, -7],
[-1, -7],
[-1, -6],
[-1, -5]]

position = [-1, -5]
danger = False
while True:
  instruction = input().rstrip().split(" ")

  if instruction[0] == "q":
      break

  if not danger:
    for i in range(int(instruction[1])):
      if instruction[0] == "l":
        position = [position[0] - 1, position[1]]
      elif instruction[0] == "r":
        position = [position[0] + 1, position[1]]
      elif instruction[0] == "u":
        position = [position[0], position[1] + 1]
      elif instruction[0] == "d":
        position = [position[0], position[1] - 1]

      if position in visited:
        danger = True
      else:
        visited.append(position)

    if danger:
      sys.stdout.write(str(position[0]) + " " + str(position[1]) + " DANGER\n")
    else:
      sys.stdout.write(str(position[0]) + " " + str(position[1]) + " safe\n")

#completed 1/31/2020
#notes: i used a list of lists which is bad but top python kiddo used sets? look into how sets would improve speed please, thanks myself