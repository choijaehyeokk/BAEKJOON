# import sys
#
# result: int = 0
# N = int(sys.stdin.readline().rstrip())
# #N * N 짜리의 상태 공간을 생성한다.
# board = [[0] * N for _ in range(N)]
#
# #현재 놓는 노드가 유망한지(promising, valid) 판단하여 백트래킹할때 pruning을 적용한다.
# #따라서 하위(자식) 노드로는 내려가지 않는다.
# #이 함수가 백트래킹의 핵심인 promising 함수.
# def isValid(row: int, column: int)-> bool:
#     for i in range(row):
#         for j in range(N):
#             if abs(i-row) == abs(j-column) and board[i][j] == 1: return False
#             elif j == column and i != row and board[i][j] == 1: return False
#     return True
#
# #깊이 우선탐색을 하면서 하위자식 즉, 다음 행을 하나씩 증가하면서 번호를 찍어준다.
# def dfs(row: int):
#     global result, board
#     if row == N:
#         result += 1
#         return
#     for column in range(N):
#         board[row][column] = 1
#         if isValid(row, column):
#             dfs(row + 1)
#             board[row][column] = 0
#         else:
#             board[row][column] = 0
#
# for i in range(N):
#     board[0][i] = 1
#     dfs(1)
#     board[0][i] = 0
# print(result)
#
# '''
# 알고리즘 출력은 성공했으나,
# 시간초과,,,
# '''
import sys

N = int(sys.stdin.readline().rstrip())
col = [0] * (N + 1)
result: int = 0
def isValid(i, col):
    k = 1
    while k < i:
        if (col[i] == col[k] or i - k == abs(col[i] - col[k])):
            return False
        k += 1
    return True

def dfs(i, col):
#열 col이라는 List로 주어지게 됨.
# col list는 valid한 노드들이 찍혀있을 것임.
# 바로, index가 행, col[index]가
    global result
    n = len(col) - 1

    #i번째 위치와 col list 에 있는 값들을 확인하면서 promising 한지 체크한다.
    if isValid(i, col):
        if i == n : result += 1
        else:
            for j in range(1, n + 1):
                col[i+1] = j
                dfs(i+1, col)
dfs(0, col)
print(result)