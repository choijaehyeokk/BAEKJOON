import sys

N, X = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for num in range(N):
    if numbers[num]  < X : print(numbers[num], end=' ')
