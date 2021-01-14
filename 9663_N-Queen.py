import sys
N = int(sys.stdin.readline().rstrip())
board = [[0] * N for _ in range(N)]
result: int = 0

for i in range(N):
    board[0][i] = 1
    if i == 0 or i == N-1 :
        pass
    else:
        pass
