import sys
import collections as c

def read():
    return sys.stdin.readline().rstrip()

maxWeight = int(read())
bridge = c.deque()
cars = 0
finalWeight = -1

totalCars = read()
for car in range(int(totalCars)):
    if finalWeight != -1:
        read()
        continue
    else: 
        if len(bridge) == 4:
            bridge.popleft()
        
        bridge.append(int(read()))

        currentWeight = 0
        for i in bridge:
            currentWeight += i

        if currentWeight > maxWeight:
            finalWeight = cars
        else:
            cars += 1

if finalWeight != -1:
    sys.stdout.write(str(finalWeight))
else:
    sys.stdout.write(totalCars)

#completed 11/12/2019
#notes: queue practice 