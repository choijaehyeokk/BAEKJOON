import sys
N = int(sys.stdin.readline().rstrip())
board = [[0]*101 for _ in range(101)]
paper: int = 1
result : int = 0
for _ in range(N):
   x, y , width, height = map(int, sys.stdin.readline().split())
   for a in range(x, width+x):
       for b in range(y, height+y):
            board[a][b] = paper
   paper += 1

for i in range(1, paper):
    for j in range(101):
        result += board[j].count(i)
    print(result)
    result = 0
