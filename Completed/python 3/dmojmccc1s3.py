import sys

input = sys.stdin.readline

strings = []
start = input().rstrip().split(" ")
strings.append(start[0])

for i in range(int(start[1])):
  response = input().rstrip().split(" ")
  if response[0] == "C":
    strings.append(strings[int(response[1])-1] + response[2])

  else:
    broke = False
    best = [-1, -1]

    for string in range(len(strings)):
      prefix = response[1]
      if best[0] == -1 or len(strings[string]) >= best[0]:
        for letter in range(len(prefix)):
          if (strings[string].startswith(prefix)):
            if len(prefix) > best[0]: 
              best = [len(prefix), string+1]
              broke = True
            elif len(prefix) == best[0] and string+1 < best[1]:
              best = [len(prefix), string+1]
              broke = True
            break
          else:
            prefix = prefix[:-1]
    
    if not broke:
      sys.stdout.write("-1\n")
    else:
      sys.stdout.write(str(best[1]) + "\n")

#tle-ing i guess im just bad