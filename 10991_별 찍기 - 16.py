import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    print(' '*(N-i-1), end='')
    for j in range(i+1):
        if j == i: print('*'); break
        print('*' + ' ', end='')