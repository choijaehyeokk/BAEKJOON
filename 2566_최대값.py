import sys

board: list = []
for i in range(9):
    column = list(map(int, sys.stdin.readline().split()))
    board.append(column)
max_value: int = -sys.maxsize
x_index: int = 0
y_index: int = 0
for i in range(9):
    if max_value < max(board[i]):
        x_index = i+1
    max_value = max(max(board[i]), max_value)
print(max_value)
for i in range(9):
    if max_value == board[x_index-1][i]:
        y_index = i+1
        break
print(x_index, y_index)
