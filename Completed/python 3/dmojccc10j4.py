import sys
input = sys.stdin.readline
testcase = input().rstrip()
while testcase != "0":
    newTestcase = list(map(int, testcase.split(" ")))

    temps = newTestcase[0]
    adjusts, pattern, temp = [],[],[]
    patLength = 0

    for case in range(len(newTestcase)-2):
        adjusts.append(newTestcase[case + 2] - newTestcase[case + 1])

    for i in adjusts:
        if i not in pattern:
            pattern.append(i)
            patLength += 1
        else:
            brokeEarly = False
            patCheck = []
            for j in range(len(adjusts) - len(pattern)):
                patCheck.append(adjusts[j + len(pattern)])
                if len(patCheck) == len(pattern):
                    if patCheck == pattern:
                        patCheck = []
                    else:
                        brokeEarly = True
                        break

            if not brokeEarly:  
                offset = 0
                for i in range(len(patCheck)):
                    offset += 1
                    if not patCheck[i] == pattern[i]:
                        patLength += offset
                        offset = 0
                break
            else:
                pattern.append(i)
                patLength += 1

    sys.stdout.write(str(patLength) + "\n")

    testcase = input().rstrip()

#completed 12/6/2019
#notes: I started this like a year ago and never got around to finishing it but it was a tricky problem...
#       also this feels really slow and inefficient but according to DMOJ best answers its only 0.05ms away from
#       best so maybe python is just bad