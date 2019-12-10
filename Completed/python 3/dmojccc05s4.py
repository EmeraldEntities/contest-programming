import sys, collections
input = sys.stdin.readline

cases = int(input())
for case in range(cases):
    contacts = collections.defaultdict(list)
    messages = int(input())
    person = input()
    sTime = 10
    for _ in range(messages - 1):
        sTime += 10
        person2 = input()
        if person2 not in contacts[person]:
            contacts[person].append(person2)
        if person not in contacts[person2]:
            contacts[person2].append(person)
        person = person2

    bsf = collections.deque()
    visited = [person]
    bsf.append([person, 0])
    saveTime = 0

    while len(bsf) > 0:
        target = bsf.popleft()
        contact = contacts[target[0]]
        for x in contact:
            if x not in visited:
                bsf.append([x, target[1] + 10])
                visited.append(x)
        
        saveTime = target[1]

    sys.stdout.write(str(sTime - (saveTime * 2)) + "\n")

#completed 12/8/19
#notes: wow im super tired and this seems super inefficient but it works so yay