import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
X, Y = 0, 0
arr = [[0] * (N) for _ in range(N)]

i, j = 0, N-1
k, z = 0, N-1
while i <= j:
    start = N * N
    for a in range(i, j+1):
        arr[a][i] = start
        if start == M:
            X, Y = a, i
        start -= 1

    for b in range(i+1, j+1):
        arr[j][b] = start
        if start == M:
            X, Y = j, b
        start -= 1
    i += 1
    j -= 1
    N -= 2

while k < z:
    start = arr[k+1][k+1] + 1
    for a in range(k+1, z+1):
        arr[k][a] = start
        if start == M:
            X, Y= k, a
        start += 1
    for b in range(k+1, z):
        arr[b][z] = start
        if start == M:
            X, Y = b, z
        start += 1
    k += 1
    z -= 1
for A in arr:
    print(*A)
print(X+1, Y+1)