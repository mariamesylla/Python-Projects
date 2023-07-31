#Magnan Sylla
#Question 1

for i in range (100):
    if (i%7==0) and (i%3 ==0) and (i%9!=0):
        print(i,end=' ')
        
#or ...

print()
for i in range (0,100,21):
    if (i%9 !=0) :
        print(i)
