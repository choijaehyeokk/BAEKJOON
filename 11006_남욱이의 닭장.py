import sys
test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    U = M*2-N
    T = M - U
    print(U, T)