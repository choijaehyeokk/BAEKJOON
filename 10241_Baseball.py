import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    Y_total: int = 0
    K_total: int = 0
    for i in range(9):
        Y, K = map(int, sys.stdin.readline().split())
        Y_total += Y
        K_total += K
    if K_total > Y_total: print('Korea')
    elif Y_total > K_total: print('Yonsei')
    else: print('Draw')
