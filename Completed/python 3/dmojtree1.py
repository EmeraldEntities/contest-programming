import sys

total = 0

graph = [[] for x in range(4)]

for i in range(4):
    tempList = sys.stdin.readline().rstrip().split(" ")
    for j in range(4):
        if tempList[j] == "1":
            graph[i].append(j)
            total += 1

offset = 0

for x in graph:
    if x == []:
        offset += 1

if total / 2.0 == 3 - offset:
    sys.stdout.write("Yes")
else:
    sys.stdout.write("No")

#completed 11/20/2019
#notes: I started this one back when I was super bad with graph theory, and just came back to make it actually
#       work.
#notes 2: also for some reason sys.stdout.write() was slower than print()? only by a few milliseconds though.