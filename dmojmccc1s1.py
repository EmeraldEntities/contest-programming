import sys

input = sys.stdin.readline

cards = int(input())

cards1 = list(map(int, input().rstrip().split(" ")))
cards2 = list(map(int, input().rstrip().split(" ")))

battles = 0
start = False
for x in range(cards):
  if cards1[x] == cards2[x] and not start:
    battles += 1
    start = True
  elif cards1[x] != cards2[x]:
    start = False

sys.stdout.write(str(battles))

#completed 2/11/2020
#notes: i needed to see how fast i could do an s1... this took me around 10 minutes..... end me 
#notes2: also check ur conditionals lmao