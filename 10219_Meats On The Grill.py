import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [['.']*W for _ in range(H)]

    for j in range(H):
        string = list(sys.stdin.readline().rstrip())
        for i in range(len(string)):
            board[j][i] = string[i]
    for k in range(H-1, -1,-1):
        for z in range(W):
            print(board[k][z],end='')
        print()