import sys

def read():
    return sys.stdin.readline().rstrip()

people = int(read())
pear = read().split(" ")
apple = read().split(" ")

result = "good"

for i in range(people):
    if result == "bad":
        continue

    appearances = 0

    for j in range(len(apple)):
        if pear[i] == apple[j]:
            appearances += 1
            if pear[j] != apple[i]:
                result = "bad"
        
        if pear[i] == apple[i] or pear[j] == apple[j]:
            result = "bad"

    if appearances > 1 or appearances == 0:
        result = "bad"

sys.stdout.write(result)

#completed 11/13/2019
#notes: idek if this is best solution