import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N-1): print(' '* (N-i-1) + '*'*(i+1))
print('*' * N)
for i in range(N-1): print(' '*(i+1) + '*'*(N-i-1))