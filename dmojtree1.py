import sys

total = 0

for i in range(4):
    tempList = sys.stdin.readline().rstrip().split(" ")
    for j in range(4):
        if tempList[j] == "1":
            total += 1

if total / 2.0 == 3:
    print("Yes")
else:
    print("No")
