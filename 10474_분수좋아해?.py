import sys
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0: break
    if M > N : print("{0} {1} / {2}".format(0,N,M))
    else: print("{0} {1} / {2}".format(N // M ,int(N%M),M))
