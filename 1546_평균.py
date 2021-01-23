import sys
N = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().split()))
max_s = max(scores)
print((sum(scores)*100 / max_s) / N)