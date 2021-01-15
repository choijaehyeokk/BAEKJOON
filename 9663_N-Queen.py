import sys

result: int = 0
N = int(sys.stdin.readline().rstrip())
board = [[0] * N for _ in range(N)]

def isValid(row: int, column: int)-> bool:
    for i in range(row):
        for j in range(N):
            if i == row and board[i][j] == 1: print('1'); return False #같은 형일때
            if abs(i-row) == abs(j-column) and board[i][j] == 1: print('2');return False #대각선일때
            if j == column and i != row and board[i][j] == 1: print('3');return False #수직거리일때
    return True

def dfs(row: int):
    global result, board
    print('=====result====== : %d' %(result))
    print('=====row====== : %d' %(row))
    if row == len(board) - 1:
        result += 1
        print('check ! {0}'.format(board))
        board = [[0] * N for _ in range(N)]

    for i in range(len(board)):
        board[row][i] = 1
        print(board, end='')
        if isValid(row, i):
            dfs(row + 1)
            print('True')
        else:
            board[row][i] = 0
            print('False')

for i in range(N-1):
    board[0][i] = 1
    dfs(1)
    board[0][i] = 0

print(result)


