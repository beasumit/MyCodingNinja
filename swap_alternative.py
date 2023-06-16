def swapalternate(a):
    n=len(a)
    for i in range(0,n-1,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    


t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    swapalternate(a)
    print(*a)
    t-=1