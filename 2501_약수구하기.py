import sys

N, M = map(int, sys.stdin.readline().split())
count: list = []
for i in range(1, N+1):
    if N % i == 0: count.append(i)
    if count == M:
        break

if M <= len(count) : print(count[M-1])
else: print(0)

