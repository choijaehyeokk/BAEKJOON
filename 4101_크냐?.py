import sys
while True:
    N, M = map(int,sys.stdin.readline().split())
    if N == 0 and M == 0: break
    print('Yes' if N > M else 'No')