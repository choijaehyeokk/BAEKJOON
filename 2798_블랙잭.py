import sys
N, M = map(int,sys.stdin.readline().split())
cards = sorted(list(map(int, sys.stdin.readline().split())))
scores: list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            current_score = cards[i] + cards[j] + cards[k]
            if current_score <= M : scores.append(current_score)
            else: break
print(max(scores))

