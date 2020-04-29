import sys

input = sys.stdin.readline

def findPermutes(yString):
  newStrings = []
  for x in range(len(yString)):
    print("letter to shift:", yString[x])
    for y in range(len(yString)):
      print("replacement letter:", yString[y])
      if x != y:
        print(yString[:y])
        print(yString[y])
        print(yString[y+1:y])
        print(yString[x])
        print(yString[x+1:])
        print("-----------")
        swap = yString[:y] + yString[y] + yString[x+1:y] + yString[x] + yString[y+1:]
        print("full = ", swap)
        if swap not in newStrings:
          newStrings.append(swap)
    
  return newStrings

print(findPermutes("bag"))

#lmao doesn't even work and I didnt have time yikes