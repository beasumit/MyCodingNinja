def fib(n)->int:
    dict = {0:0, 1:1}
    for i in range(2,n+1):
        dict[i] = dict[i-1]+dict[i-2]
    
    return dict[n]

x = fib(4)
print(x)
#finish