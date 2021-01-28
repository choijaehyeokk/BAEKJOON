import sys
N, M = map(str, sys.stdin.readline().split())
print(format(int(N, 2) + int(M, 2), 'b'))