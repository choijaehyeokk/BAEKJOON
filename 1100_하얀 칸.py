import sys
board: list = []
result: int = 0
for _ in range(8):
    board.append(sys.stdin.readline().rstrip())

for i in range(len(board)):
    #line is string
    line = board[i]
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if line[j] == 'F' : result += 1
    else:
        for j in range(8):
            if j % 2 != 0:
                if line[j] == 'F' :result += 1
print(result)

