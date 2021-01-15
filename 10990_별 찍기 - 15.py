import sys
N = int(sys.stdin.readline().rstrip())
k:int = 1
for i in range(N):
    if i == 0: print(' '*(N-1) +'*')
    else:
        print(' '*(N-i-1) + '*' + ' '* (k), end='')
        print('*')
        k += 2
