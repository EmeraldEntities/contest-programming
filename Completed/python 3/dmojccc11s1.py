import re, sys, string

totNum = int(sys.stdin.readline())

allSentence = ""

for sentence in range(totNum):
    allSentence = allSentence + (sys.stdin.readline().rstrip("\n")) + " "

allSentence = allSentence.lower()

allS = re.findall(r's', allSentence)
allT = re.findall(r't', allSentence)

language = "English" if len(allT) > len(allS) else "French"
sys.stdout.write(language)

#completed 8/29/2019
#notes: wow re is fun and also pay attention to the question