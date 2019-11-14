import sys

def read():
    return sys.stdin.readline().rstrip()

number = int(read())
counter = 0
counterFound = False

# def recurseCalc(number):
#     if number == 1:
#         return 0
    
#     if number % 2 == 0:
#         return 1 + recurseCalc(number / 2)
#     else:
#         return 1 + recurseCalc((number * 3) + 1)

# sys.stdout.write(str(recurseCalc(number)))

while not counterFound:
    if number == 1:
        counterFound = True
    else:
        counter += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1

sys.stdout.write(str(counter))

#completed 11/13/2019
#notes: recursion seemed the worse case, finishing a bit slower (0.004 seconds) and using 0.24 MB more ram...