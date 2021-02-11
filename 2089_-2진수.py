import sys, math
import collections
N = int(sys.stdin.readline().rstrip())
result = collections.deque()
A = ''
if N == 0: print(0)
else:
    while N != 0:
        result.appendleft(abs(N%-2))
        N = math.ceil(N / -2)
    for i in result:
        A += str(i)
    print(A)

