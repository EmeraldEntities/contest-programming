firstGroup = input()
secondGroup = input()

secondAdjustableGroup = list(secondGroup)

failed = False
popped = False

letters = []
for i in list(firstGroup):
    letters.append(i)

for i in range(len(secondAdjustableGroup)-1, -1, -1):
    popped = False
    if secondAdjustableGroup[i] == "*":
        continue

    for j in range(len(letters)-1, -1, -1):
        if popped:
            continue
        if secondAdjustableGroup[i] == letters[j]:
            letters.pop(j)
            secondAdjustableGroup.pop(i)
            popped = True
        
    if not popped:
        failed = True

if failed:
    print("N")
else:
    if len(secondAdjustableGroup) == len(letters):
        print("A")
    else:
        print("N")

#Done 08/08/19 (M/D/Y)