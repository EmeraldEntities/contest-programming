m1 = input().split(" ")
m2 = input().split(" ")

def add(m1, m2):
    newM = []
    for i in zip(m1, m2):
        newM.append(i[0] + i[1])
    

print(add(m1, m2))