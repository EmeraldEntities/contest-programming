import sys
from collections import defaultdict, deque

input = sys.stdin.readline
graph = defaultdict(list)

newRoad = input().rstrip()

while newRoad != "**":
    road = list(newRoad)
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

    newRoad = input().rstrip()

#im stuck idk