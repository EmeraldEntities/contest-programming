import sys

answers = []

def read():
    return sys.stdin.readline().rstrip()

for case in range(int(read())):
    branch = []
    start = []
    allCars = 0
    for i in range(int(read())):
        allCars += 1
        start.append(read())

    total = 1
    notFound = True
    while notFound:
        if len(start) == 0:
            if int(branch[len(branch)- 1]) == total:
                branch.pop()
                total += 1
            else:
                answers.append("N")
                notFound = False
        else:
            if int(start[len(start) - 1]) == total:
                start.pop()
                total += 1
            elif len(branch) - 1 >= 0 and int(branch[len(branch)- 1]) == total:
                branch.pop()
                total += 1
            else:
                branch.append(start.pop())

        if total == allCars:
            notFound = False
            answers.append("Y")

for i in answers:
    print(i)

#completed 11/11/2019
#notes: great problem