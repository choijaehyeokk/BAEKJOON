import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
sumnumber: int = 0
for i in range(0, N):
    if i == N-1: print((i+1)*numbers[i] - sumnumber); break
    print((i+1)*numbers[i] - sumnumber, end=' ')
    sumnumber = numbers[i] * (i + 1)
