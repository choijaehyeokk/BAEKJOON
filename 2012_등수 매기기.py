import sys

N = int(sys.stdin.readline().rstrip())
result = 0
exp_score = []
for _ in range(N):
    exp = int(sys.stdin.readline().rstrip())
    exp_score.append(exp)
exp_score.sort()

for i in range(N):
    result += abs(exp_score[i] -(i+1))
print(result)

