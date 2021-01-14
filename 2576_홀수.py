import sys
odds: list = []
for i in range(7):
    N = int(sys.stdin.readline().rstrip())
    if N % 2 != 0: odds.append(N)
if not odds : print(-1)
else:
    print(sum(odds))
    print(min(odds))