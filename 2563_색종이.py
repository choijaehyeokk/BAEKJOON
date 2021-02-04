import sys
board = [[False] * 101 for _ in range(101)]
cnt: int = 0
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())

    for x in range(X, X+10):
        for y in range(Y, Y+10):
            if board[x][y] == False: board[x][y] = True

for b in board:
    cnt += b.count(True)
print(cnt)