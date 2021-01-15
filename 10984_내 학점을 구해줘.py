import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    total_C: int = 0
    total_G: float = 0
    for j in range(N):
        C, G = map(float, sys.stdin.readline().split())
        total_C += C
        total_G += C*G
    print("{0} {1}".format(int(total_C), round(total_G/total_C,1)))