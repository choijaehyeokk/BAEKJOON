import sys
N = int(sys.stdin.readline().rstrip())
if N == 0 or N == 1: print(1)
else:
    result: int = 1
    for i in range(1, N+1):
        result *= i
    print(result)