import sys

def read():
    return sys.stdin.readline().rstrip()

sensors = {}

for _ in range(int(read())):
    reading = int(read())
    if reading in sensors.keys():
        sensors[reading] += 1
    else:
        sensors[reading] = 1

sortedSensors = sorted(sensors.items(), key = lambda x: (x[1], x[0]), reverse = True)
bestFrequency = sortedSensors[0][1]
secondBest = 1
frequent, secondFrequent = [], []
foundSecond = False

for test in sortedSensors:
    if foundSecond:
        if test[1] == secondBest:
           secondFrequent.append(test[0])
        else:
            continue

    if test[1] != bestFrequency:
        secondBest = test[1]
        secondFrequent.append(test[0])
        foundSecond = True
    else:
        frequent.append(test[0])

if len(frequent) == 1:
    if not foundSecond:
        secondFrequent = frequent[::]

    minTest = abs(frequent[0] - max(secondFrequent))
    maxTest = abs(frequent[0] - min(secondFrequent))
    if minTest > maxTest:
        sys.stdout.write(str(minTest))
    else:
        sys.stdout.write(str(maxTest))

    # minimum = 2001
    # maximum = 0
    # for i in secondFrequent:
    #     if i > maximum:
    #         maximum = i
    #     if i < minimum:
    #         minimum = i

    # minTest = abs(frequent[0] - minimum)
    # maxTest = abs(frequent[0] - maximum)
    # if minTest > maxTest:
    #     sys.stdout.write(str(minTest))
    # else:
    #     sys.stdout.write(str(maxTest))
else:
    sys.stdout.write(str(abs(max(frequent) - min(frequent))))

#completed 11/14/2019
#notes: almost TLE-d on this one with the last test case taking 3.5 out of 5... maybe work on optimizing this one more?
#       it is pretty... scuffed...
#notes 2: also I tried making it go faster by trying to find the min/max in one for loop, and it kinda worked?