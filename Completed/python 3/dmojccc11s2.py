import sys

totalNum = int(sys.stdin.readline())
tQue = []
tAns = []

for i in range(totalNum):
    tQue.append(sys.stdin.readline())

for i in range(totalNum):
    tAns.append(sys.stdin.readline())

correct = 0

for ans in zip(tQue, tAns):
    if ans[0] == ans[1]:
        correct += 1

sys.stdout.write(str(correct))

#completed 8/29/2019
#notes: sys.stdin.readline() worked for some reasom...?