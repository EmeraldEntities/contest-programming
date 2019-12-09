import sys

def read():
    return sys.stdin.readline().rstrip()

def write(thing):
    sys.stdout.write(thing)

students = int(read())
friendships = {}

for _ in range(students):
    currentStudent = list(map(int, read().split(" ")))
    friendships[currentStudent[0]] = currentStudent[1]

notFound = True
answers = []

currentAssignment = list(map(int, read().split(" ")))
while currentAssignment != [0, 0]:
    visited = []

    currentFriend = friendships.get(currentAssignment[0])
    notFound = True
    seperation = 0
    while notFound:
        if currentFriend == currentAssignment[1]:
            notFound = False
            answers.append(seperation)
        elif currentFriend in visited:
            notFound = False
            answers.append(-1)
        else:
            seperation += 1
            visited.append(currentFriend)
            if (currentFriend in friendships.keys()):
                currentFriend = friendships.get(currentFriend)
            else:
                notFound = False
                answers.append(-1)

    currentAssignment = list(map(int, read().split(" ")))
    
for answer in answers:
    toPrint = "Yes " + str(answer) + "\n" if answer != -1 else "No\n"
    write(toPrint)

#completed 12/8/19
#notes: this ran pretty slow so maybe i should try to speed it up and make it take less memory
#       also normal dict and default dict dont really change much in terms of runtmie
#       also please use true or at least 1 and 0, myself