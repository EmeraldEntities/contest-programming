import sys

input = sys.stdin.readline

bloodRecievable = {
  0: [0],             #o neg
  1: [1, 0],          #o pos
  2: [2, 0],          #a neg
  3: [3, 2, 1, 0],    #a pos
  4: [4, 0],          #b neg
  5: [5, 4, 1, 0],    #b pos
  6: [6, 4, 2, 0],     #ab-neg
  7: [7, 6, 5, 3, 4, 2, 1, 0]#ab-pos
}

bloodAmount = []

l = input().rstrip().split(" ")
for i in l:
  bloodAmount.append(int(i))  #lets get all the amount of blood

savedPatients = 0
l = input().rstrip().split(" ")
for i in range(len(l)):
  bloodRecieve = bloodRecievable.get(i)  #retrieve what blood this batch of patients can recieve
  index = 0
  amount = int(l[i])
  while amount != 0 and index < len(bloodRecieve):
    if bloodAmount[bloodRecieve[index]] != 0:
      if (bloodAmount[bloodRecieve[index]] >= amount):
        bloodAmount[bloodRecieve[index]] -= amount
        savedPatients += amount
        amount = 0
      else:   #if we have less blood available than patients who need, increase blood search index by one
        savedPatients += bloodAmount[bloodRecieve[index]]
        amount -= bloodAmount[bloodRecieve[index]]
        bloodAmount[bloodRecieve[index]] = 0
        index += 1 
    else:
      index += 1

sys.stdout.write(str(savedPatients))

#completed 1/23/20
#notes: don't underestimate the power of missing a -=...