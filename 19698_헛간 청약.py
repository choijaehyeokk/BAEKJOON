import sys

N, W, H, L = map(int, sys.stdin.readline().split())
maxinum = (W // L) * (H // L)

if maxinum >= N: print(N)
else:
    print(maxinum)