import sys
R, C = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())
result_X, result_Y = 0, 0
arr = [[0] * R for _ in range(C)]
def make_stat(A: list):
    global result_Y, result_X
    i = 1
    x, y, z = C - 1, 0, R - 1
    while i<= C * R:
        for a in range(x, y-1, -1):
            A[a][y] = i
            if i == K: result_X, result_Y = a, y
            i += 1
        for b in range(y+1, z+1):
            A[y][b] = i
            if i == K: result_X, result_Y = y, b
            i+= 1
        for c in range(y+1, x):
            A[c][z] = i
            if i == K: result_X, result_Y = c, z
            i+= 1
        for d in range(z, y, -1):
            A[x][d] = i
            if i == K: result_X, result_Y = x, d
            i+= 1
        x -= 1
        y += 1
        z -= 1

if K > C*R: print(0)
else:
    make_stat(arr)
    print(C-result_X, result_Y+1)