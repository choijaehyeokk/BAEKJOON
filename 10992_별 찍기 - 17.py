import sys
N = int(sys.stdin.readline().rstrip())
k:int = 1
for i in range(N-1):
    print(' ' * (N - i - 1), end='')
    if i == 0: print('*')
    else: print('*', end='')
    if i > 0: print(' '* k + '*'); k += 2
print('*'* (2*N - 1))