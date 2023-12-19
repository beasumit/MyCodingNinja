n = int(input())
a = int(input())
product = 1 
sum = 0 
if a == 2 : 
   for number in range(1,n+1): 
       product *= number 
   print(product) 
elif a == 1: 
   for number in range(1,n+1): 
       sum += number 
   print(sum)        
else:  
   print("-1") 