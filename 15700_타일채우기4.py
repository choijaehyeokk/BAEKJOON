import sys

N, M = map(int, sys.stdin.readline().split())

count : int = 0
count += (N // 2) * M

if N % 2 != 0 :
    count += (M // 2)
print(count)