import sys

N = int(sys.stdin.readline().rstrip())
while True:
    M = int(sys.stdin.readline().rstrip())
    if M == 0 : break
    print('{0} is a multiple of {1}.'.format(M, N) if M % N == 0 else '{0} is NOT a multiple of {1}.'.format(M, N))