import sys

input = sys.stdin.readline

levers = int(input().rstrip())
map_of_levers = list(input().rstrip())

def main():
    inv = 0
    check = ["1", "0"]
    
    total = 0
    for i in range(levers-1, -1, -1):
        if (map_of_levers[i] == check[inv]):
            total += 1
            inv = (inv + 1) % 2

    sys.stdout.write(str(total))

main()

#completed 07/08/2020
#notes: did this one to help out a friend