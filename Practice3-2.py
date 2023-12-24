count = int(input("Enter Count Of Numbers:"))
Numbers=[]
for i in range(count):
  x = int(input("Enter Number{0}:".format(i+1)))
  Numbers.append(x)
y = Numbers[:]
y.sort()
if y == Numbers:
  print("It is sort")
  print(Numbers)
  print(y)
else:
  print("it isnt sort")  
  print(Numbers)
  print(y)