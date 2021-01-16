import sys
testcase = int(sys.stdin.readline().rstrip())
for i in range(testcase):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)