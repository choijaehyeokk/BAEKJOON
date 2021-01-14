import sys

testcase = int(sys.stdin.readline().rstrip())
for i in range(testcase):
    H, W, N = map(int, sys.stdin.readline().split())
    floor, ho  = N % H, N // H
    if floor == 0: print(H * 100 + ho)
    else: print((floor)*100 + (ho + 1))
