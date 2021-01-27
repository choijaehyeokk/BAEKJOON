import sys, math
N, W, H = map(int, sys.stdin.readline().split())
for i in range(N):
    length = int(sys.stdin.readline().rstrip())
    if math.sqrt(pow(W,2)+pow(H,2)) >= length: print('DA')
    else: print('NE')