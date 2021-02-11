import sys
T = int(sys.stdin.readline().rstrip())
max_univ = ''
max_value = -sys.maxsize
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        A, B = map(str, sys.stdin.readline().split())
        if max_value < int(B):
            max_value = int(B)
            max_univ = A
    print(max_univ)