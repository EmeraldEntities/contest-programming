import sys

words = list(sys.stdin.readline().rstrip("\n"))
acceptable = ["I", "O", "S", "H", "Z", "X", "N"]

canWork = True

for i in words:
    if i not in acceptable:
        canWork = False

if canWork:
    print("YES")
else:
    print("NO")

#completed 9/5/2019
#notes: surprisingly easy