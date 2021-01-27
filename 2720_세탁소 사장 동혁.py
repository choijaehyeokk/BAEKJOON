import sys
test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    cent = int(sys.stdin.readline().rstrip())
    A = cent//25
    cent %= 25
    B = cent // 10
    cent %= 10
    C = cent // 5
    cent %= 5
    D = cent // 1
    print("{0} {1} {2} {3}".format(A,B,C,D))
