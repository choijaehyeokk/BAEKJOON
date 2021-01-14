import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, N, M, N+M))