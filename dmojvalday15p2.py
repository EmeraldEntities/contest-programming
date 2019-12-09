import sys
input = sys.stdin.readline

numCages, totalMinutes = map(int, input().split())
cages = []

for i in range(numCages):
    x, y = map(int, input().split())
    cages.append([x, y, 0])

#suspended cause i cant actually think rn omg        