import sys
testcase = int(sys.stdin.readline().rstrip())
for i in range(testcase):
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    print(sum(numbers))
