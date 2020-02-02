import sys

input = sys.stdin.readline

def recurse(length):
  l = length
  

limit = 0
for i in range(int(input().rstrip())):
  info = list(map(int, input().rstrip().split(" ")))
  limit = info[1]
  length = info[0]