#این برنامه رو میشه با دو روش نوشت که یک روش رو کامنت کردم
L = int(input("Enter the lenght of snake:"))
for i in range (L):
    if i %2==0:
        print("*", end="")
    else:
        print("#", end="")
          
        
        #.............................................................
       
       
#L = int(input("Enter the lenght of snake:"))
#snake=[]
#for i in range (L):
    #if i %2==0:
        #snake.append("#",end="")
    #else:
       # snake.append("*",end="")
    #print("your snake :) --->" ,snake)    