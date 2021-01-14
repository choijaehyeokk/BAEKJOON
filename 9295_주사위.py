import sys

test_case = int(sys.stdin.readline().rstrip())
for i in range(test_case):
    A, B = map(int, sys.stdin.readline().split())
    print("Case {0}: {1}".format(i+1, A+B))