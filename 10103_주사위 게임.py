import sys
T = int(sys.stdin.readline().rstrip())
S: int = 100
C: int = 100
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if M > N : C -= M
    elif M < N : S -= N
print(C)
print(S)