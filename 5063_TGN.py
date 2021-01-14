import sys

test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    R, E, C = map(int, sys.stdin.readline().split())
    if R == (E-C) : print('does not matter')
    else: print('advertise' if (E-C) > R else 'do not advertise')