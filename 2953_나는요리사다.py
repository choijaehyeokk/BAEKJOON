import sys
max_index: int = -sys.maxsize
max_score: int = -sys.maxsize
for i in range(5):
    score = list(map(int, sys.stdin.readline().split()))
    current_score = sum(score)
    if current_score > max_score:
        max_score = current_score
        max_index = i + 1
print(max_index, max_score)