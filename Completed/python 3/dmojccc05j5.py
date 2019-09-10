import sys

def findMonkeyWord(word, layer = 0, bCount = 0, isValid = True, previousLetter = None):
    if not isValid:
        return isValid
    if len(word) == 0:
        if bCount != 0:
            isValid = False
        return isValid
    
    layer += 1
    if layer == 1:
        if word[0] == "B":
            bCount += 1
        elif word[0] != "A":
            isValid = False

    else:
        if previousLetter == "A":
            if word[0] == "S":
                bCount -= 1
                if bCount < 0:
                    isValid = False
            elif word[0] != "N":
                isValid = False
        elif previousLetter == "N" or previousLetter == "B":
            if word[0] == "B":
                bCount += 1
            elif word[0] != "A":
                isValid = False
        else:  #if the previous letter was S
            if word[0] == "S":
                bCount -= 1
                if bCount < 0:
                    isValid = False
            elif word[0] != "N":
                isValid = False

    isValid = findMonkeyWord(word[1:], layer, bCount, isValid, word[:1])
    return isValid

newWord = "O"
while newWord != "X":
    newWord = sys.stdin.readline().rstrip("\n")
    if newWord != "X":
        result = findMonkeyWord(newWord)
        toPrint = "YES\n" if result else "NO\n"
        sys.stdout.write(toPrint)

#completed 8/9/2019
#notes - that was actually kinda fun :))
#notes 2 - I actually might redo some of this stuff honestly its really bad recursion