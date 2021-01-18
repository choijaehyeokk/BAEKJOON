import sys, math
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
for i in range(N):
    if B >= A[i]:
        A[i] = 0
    else:
        A[i] -= B
        A[i] = math.ceil((A[i] / C))
print(sum(A) + N)