import sys

R, C = map(int, sys.stdin.readline().split())
board = [[False for _ in range(C+2)]]
visited = []
max_cnt = -1
for _ in range(R):
    line = [False]
    line.extend(list(sys.stdin.readline().rstrip()))
    line.append(False)
    board.append(line)
board.append([False for _ in range(C+2)])

def bfs(board, x, y):
    global  max_cnt
    queue = set()
    queue.add((x,y, board[x][y]))
    pos_x = [0, -1, 1, 0]
    pos_y = [-1, 0, 0, 1]
    while queue:
        x, y, alpabets = queue.pop()
        if max_cnt < len(alpabets): max_cnt = len(alpabets)

        for i in range(4):
            new_x = x + pos_x[i]
            new_y = y + pos_y[i]
            if board[new_x][new_y] is False or board[new_x][new_y] in alpabets:
                continue
            else:
                queue.add((new_x, new_y, alpabets + board[new_x][new_y]))
            #갈 수 있나? -> 위 코드와 다른점, 일단 가서 판단하는 것이 아님

bfs(board, 1, 1)
print(max_cnt)


#print(board)
# def bfs(board, x, y, cnt):
#     global max_cnt
#     alpabet = board[x][y]
#
#     pos_x = [0,-1,1,0]
#     pos_y = [-1,0,0,1]
#     if alpabet in visited or alpabet is False:
#         if max_cnt < cnt-1:
#             max_cnt = cnt-1
#         return
#     else:
#         visited.append(alpabet)
#         for i in range(4):
#             bfs(board, x+ pos_x[i], y + pos_y[i], cnt+1)
#         visited.remove(alpabet)