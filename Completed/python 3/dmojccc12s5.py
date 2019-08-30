import sys

dimensions = list(map(int, sys.stdin.readline().split(" "))) # Get the dimensions of maze
#list comprehension for making the lab, with a buffer of one extra row and column so we don't list out of index
lab = [[0 for column in range(dimensions[1] + 1)] for row in range(dimensions[0] + 1)] 
blocked = [[False for column in range(dimensions[1] + 1)] for row in range(dimensions[0] + 1)]

#add cats
for cat in range(int(sys.stdin.readline())):
    catLocation = list(map(int, sys.stdin.readline().split(" ")))
    blocked[catLocation[0]][catLocation[1]] = True

#set up the start
lab[1][1] = 1 #our mouse location
blocked[1][1] = 1 #set so that the code doesn't make our mouse location 0 because of it looking left and up and only finding 0 from buffers

#looks up every location and gets the total amount of routes
for row in range(1, dimensions[0] + 1):
    for column in range(1, dimensions[1] + 1):
        if not blocked[row][column]:
            lab[row][column] = lab[row][column-1] + lab[row-1][column]

print(lab)
print(lab[dimensions[0]][dimensions[1]])

#completed 8/30/2019
#notes: This felt like a bit of cheating since I had to look up an example of how to do it, but it was a good
#       learning experience. I didn't hand this into DMOJ cause i want only my work to be on there.
#explaination: This was done under the assumption that paths can be determined by looking at the number to the
#       left and top, and adding them. The numbers mean the amount of paths that converge into that square. The
#       answer is at the brother's square, as there are only two ways to reach him (top and left), meaning that
#       all possible paths must converge at some point