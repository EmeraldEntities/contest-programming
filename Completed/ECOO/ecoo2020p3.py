import sys, math
input = sys.stdin.readline


test = int(input().rstrip())
for _ in range(test):
    c = int(input().rstrip())
    for __ in range(c):
        h, w = list(map(int, input().rstrip().split(" ")))

        edit = []
        for _ in range(h):
            edit.append(input().rstrip())

        c = []
        mx, rm = 1000, -1
        count = 0
        for each in edit:
            a, b = each.find("*"), each.rfind("*")
            d = each.count("*")
            c.append([a, b, d])

            mx = a if a < mx and mx != -1 else mx
            rm = b if b > rm and rm != -1 else rm
            count = d if d > count else count

        left, middle, right = 0, 0, 0
        print (c)
        for i in range(len(c)):
            if c[i][0] == mx: left += 1 
            if c[i][1] == rm: right += 1
            if c[i][2] == count: middle += 1

        if left > h/2 and right > h/2:
            zero = middle/2.0
            eight = middle/3.0
            if int(zero) == zero and int(eight) != eight: sys.stdout.write("0")
            elif int(zero) != zero and int(eight) == eight: sys.stdout.write("8")
            else: sys.stdout.write("8")
        elif left == 0 and right > h/2 and middle == 0:
            sys.stdout.write("1")
        elif (left < h/2 and left != 0) and (right < h/2 and right != 0):
            sys.stdout.write("2")
        elif (left == 0 and right > h/2 and middle % 3 == 0):
            sys.stdout.write("3")
        elif (left < h/2 and right > h/2 and middle > 0): sys.stdout.write("4")
        elif (left < h/2 and right < h/2 and middle % 3): sys.stdout.write("5")
        elif (left > h/2 and right < h/2 and midde % 3): sys.stdout.write("6")
        elif (left == 1 and right > h/2 and middle % 3): sys.stdout.write("7")
        elif (left < h/2 and right > h/2 and middle % 2): sys.stdout.write("9")

    sys.stdout.write("\n");

#didn't finish hehehehe but this is really scuffed code


       

    
                    
