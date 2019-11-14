import sys

def read():
    return sys.stdin.readline().rstrip()

cities = {}

cityInput = True
while cityInput:
    cityData = read().split(" ")

    cities[cityData[0]] = cityData[1]

    if cityData[0] == "Waterloo":
        cityInput = False

minTemp = 201
coldestCity = None
for city in cities.items():
    if int(city[1]) < minTemp:
        coldestCity = city[0]
        minTemp = int(city[1])

sys.stdout.write(coldestCity)

#completed 11/12/2019
#notes: just did this one to test how much my score would increase