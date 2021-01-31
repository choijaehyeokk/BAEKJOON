import sys
L = int(sys.stdin.readline().rstrip())
i = int(sys.stdin.readline().rstrip())
cake = [0] * (L+1)
A = [0] * (i+1)
idx: int = 0
max_count1, max_count2 = -sys.maxsize, -sys.maxsize

for j in range(1, i+1):
    P, K = map(int, sys.stdin.readline().split())
    if K - P - 1 > max_count1:
        idx = j
        max_count1 = K - P - 1


    for k in range(P, K + 1):
        if not cake[k]:
            cake[k] = j
            A[j] += 1

print(idx)
print(A.index(max(A)))