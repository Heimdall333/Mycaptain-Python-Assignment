#1
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
       
    elif n==1: 
        return 0
   
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2) 

print(Fibonacci(9)) 

#2 a)
list1 = [12, -7, 5, 64, -14]
num = 0     
while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end = " ")
    num += 1
    
#2 b)
list2 = [12, 14, -95, 3]
num = 0     
while(num < len(list2)):
    if list2[num] >= 0:
        print(list2[num], end = " ")
    num += 1
