import sys
score: list = []
current_score: int = 0
for _ in range(10):
    score.append(int(sys.stdin.readline().rstrip()))
for i in range(len(score)):
    current_score += score[i]
    if current_score >= 100:
        A = current_score - 100
        B = 100 - (current_score - score[i])
        if B > A: print(current_score)
        elif A > B: print(current_score - score[i])
        else: print(current_score)
        break
    if i == len(score)-1:
        print(current_score)
