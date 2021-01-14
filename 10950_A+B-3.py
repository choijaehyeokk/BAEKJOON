import sys
testcase = int(sys.stdin.readline().rstrip())
for i in range(testcase):
    N, M = map(int, sys.stdin.readline().split())
    print(N+M)