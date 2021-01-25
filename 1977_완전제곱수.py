import sys
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
psn: list = []
for i in range(1, 101):
    a = i**2
    if a >= M and a <= N: psn.append(a)
if not psn: print(-1)
else:
    print(sum(psn))
    print(min(psn))