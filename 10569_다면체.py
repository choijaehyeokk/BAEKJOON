import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    V, E = map(int, sys.stdin.readline().split())
    print(E+2-V)