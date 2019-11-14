import sys

def read():
    return sys.stdin.readline().rstrip()

rivers = []
streams = int(read())

for _ in range(streams):
    rivers.append(int(read()))

notEnd = True
while notEnd:
    option = read()
    if option == "77":
        notEnd = False

    elif option == "88":
        join = int(read())
        amount = rivers.pop(join-1)
        rivers[join-1] += amount

    elif option == "99":
        split = int(read())
        percent = int(read())/100

        amount = rivers[split-1] * percent
        rivers.insert(split, rivers[split-1] - amount)
        rivers[split-1] -= rivers[split-1] * (1.00 - percent)
        
for i in range(len(rivers)):
    rivers[i] = round(rivers[i])
    sys.stdout.write(str(rivers[i]) + " ")

#completed 11/13/2019
#notes: i feel like if i used a linked list, this would go much faster, but oh well