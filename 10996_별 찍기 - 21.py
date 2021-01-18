import sys
N = int(sys.stdin.readline().rstrip())
if N == 1: print('*')
else:
    T = N
    for i in range(N):
        for j in range(T):
            if j % 2 == 0:
                if j == T-1: print('*')
                else: print('*', end='')
            else:
                if j == T-1: print(' ')
                else: print(' ',end='')
        for k in range(T):
            if k % 2 != 0:
                if k == T-1: print('*')
                else: print('*', end='')
            else:
                if k == T-1: print(' ')
                else: print(' ',end='')