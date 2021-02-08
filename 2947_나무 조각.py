import sys

numbers = list(map(int, sys.stdin.readline().split()))
def change(n: list):
    arr = n
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    return arr
while numbers != [1,2,3,4,5]:
    numbers = change(numbers)