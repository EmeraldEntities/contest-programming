import sys

input = sys.stdin.readline

observe = int(input().rstrip())
measurements = []

for i in range(observe):
  data = list(map(int, input().rstrip().split(" ")))
  measurements.append(data)

sortMeasurements = sorted(measurements, key=lambda x: x[0])

maxSpeed = 0
for x in range(len(sortMeasurements)-1):
  speed = abs((sortMeasurements[x+1][1] - sortMeasurements[x][1]))/abs((sortMeasurements[x+1][0] - sortMeasurements[x][0]))
  if speed > maxSpeed:
    maxSpeed = speed

sys.stdout.write(str(maxSpeed))

#completed