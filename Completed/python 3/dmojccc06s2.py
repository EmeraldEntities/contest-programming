plaintext = list(input())
codedText = list(input())
haveToSolve = list(input())
letters = {}

for count, i in enumerate(plaintext, start=0):
    if not i in letters.values():
        letters[codedText[count]] = i

message = ""
for i in haveToSolve:
    if i in letters.keys():
        message = message + f"{letters[i]}"
    else:
        message = message + "."

print(message)

#completed 08/10/19 (MM/DD/YY)
#note: import sys, sys.stdin.readline() and sys.stdout.write() all returned a SyntaxError on DMOJ. Strange.