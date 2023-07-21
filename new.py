from sys import stdin

def arrange(arr,n):
    left = 0
    right = n - 1
    counter = 1

    while left <= right:

        if counter%2 == 1:
            arr[left] = counter
            counter += 1
            left += 1
        else :
            arr[right] = counter
            counter += 1
            right -= 1

def printList(arr, n):
    for i in range(n):
        print(arr[i], end = ' ')
    print()

#main
t = int(stdin.readline().strip())

while t > 0:
    n = int(stdin.readline().strip())
    arr = n * [0]
    arrange(arr, n)
    printList (arr, n)
    t -= 1