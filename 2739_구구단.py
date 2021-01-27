import sys
N = int(sys.stdin.readline().rstrip())
for i in range(1, 10): print("{0} * {1} = {2}".format(N, i, N*i))