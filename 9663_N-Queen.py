import sys

result: int = 0
N = int(sys.stdin.readline().rstrip())
board = [[0] * N for _ in range(N)]
def isValid(row: int, column: int)-> bool:
    for i in range(row):
        for j in range(N):
            if abs(i-row) == abs(j-column) and board[i][j] == 1: return False
            elif j == column and i != row and board[i][j] == 1: return False
    return True

def dfs(row: int):
    global result, board
    if row == N:
        result += 1
        return
    for column in range(N):
        board[row][column] = 1
        if isValid(row, column):
            dfs(row + 1)
            board[row][column] = 0
        else:
            board[row][column] = 0

for i in range(N):
    board[0][i] = 1
    dfs(1)
    board[0][i] = 0
print(result)

'''
알고리즘 출력은 성공했으나,
시간초과,,,
'''


