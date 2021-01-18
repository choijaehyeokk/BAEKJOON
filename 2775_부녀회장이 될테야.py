import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    apart = [x for x in range(1, n+1)]
    for a in range(k):
        for b in range(1, n):
            apart[b] += apart[b-1]
    print(apart[n-1])
