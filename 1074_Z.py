import sys

N, R, C = map(int, sys.stdin.readline().split())
cnt = 0

def Z(n, r, c):
    global cnt
    if R == r and C == c:
        return print(int(cnt))
    if n == 1:
        cnt += 1
        return

    if not (r <= R < r +n and c <= C < c + n):
        cnt += n * n
        return
    #Z 왼쪽위
    Z(n/2, r, c)
    #Z 오른쪽위
    Z(n/2, r, c + (n/2))
    #Z 왼쪽아래
    Z(n/2, r + (n/2), c)
    #Z 오른쪽아래
    Z(n/2, r + (n/2), c + (n/2))
Z(2 ** N, 0, 0)