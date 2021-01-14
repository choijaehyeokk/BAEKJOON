import sys
scores = []
for i in range(5):
    score = int(sys.stdin.readline().rstrip())
    if score < 40:
        score = 40
    scores.append(score)

print(int(sum(scores)/5))