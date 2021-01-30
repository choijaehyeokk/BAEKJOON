import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    board = []
    result: int = 0
    for _ in range(M):
        board.append(list(map(int, sys.stdin.readline().split())))

    for i in range(N):
        zero_one = ""
        for k in range(M):
            zero_one += str(board[k][i])
        for j in range(M-1):
            if zero_one[j] == '0': continue
            else:
                result += list(zero_one[j+1:]).count('0')

    print(result)