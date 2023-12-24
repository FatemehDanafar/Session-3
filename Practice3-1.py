import random
count = int(input("Enter Count of number that you want be in the list:"))
Number = [random.randint(0,30)]
for i in range(count): 
    rep=(random.randint(0,30))
    if rep!=Number:
     Number.append(rep)
print("your list:", Number)

