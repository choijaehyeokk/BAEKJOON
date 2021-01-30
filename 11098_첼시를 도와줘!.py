import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    M = int(sys.stdin.readline().rstrip())
    player = []
    money = []
    for _ in range(M):
        A, B = map(str, sys.stdin.readline().split())
        player.append(B)
        money.append(int(A))
    for j in range(M):
        if max(money) == money[j]:
            print(player[j])
            break

