import sys
board = []
ref = []
check = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False,'10':False,'11':False,'12':False,
         '13':False,'14':False,'15':False,'16':False,'17':False,'18':False,'19':False,'20':False,'21':False,'22':False,'23':False,
         '24':False,'25':False}
def isbingo(check:dict, board:list)->bool:
    #가로들
    total = 0
    for a in board:
        cnt = 0
        for x in a:
            if check[str(x)]:
                cnt += 1
        if cnt == 5:
            total += 1
    #세로들
    for b in range(5):
        cnt = 0
        for x in range(5):
            if check[str(board[x][b])]:
                cnt += 1
        if cnt == 5:
            total += 1
    #대각선
    if check[str(board[0][0])] and check[str(board[1][1])] and check[str(board[2][2])] and check[str(board[3][3])] and check[str(board[4][4])]:
        total += 1
    if check[str(board[4][0])] and check[str(board[3][1])] and check[str(board[2][2])] and check[str(board[1][3])] and check[str(board[0][4])]:
        total += 1
    if total >= 3:
        return True
    else: return False

for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
    ref += (list(map(int, sys.stdin.readline().split())))

for i in range(len(ref)):
    idx = i+1
    check[str(ref[i])] = True

    if isbingo(check, board):
        print(idx)
        break