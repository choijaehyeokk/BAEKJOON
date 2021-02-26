import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
N_name = []
M_name = []
result = []
cnt = 0
for _ in range(N):
    N_name.append(sys.stdin.readline().rstrip())
for _ in range(M):
    M_name.append(sys.stdin.readline().rstrip())

name = Counter(N_name + M_name)

for k, v in name.items():
    if v == 2:
        cnt += 1
        result.append(k)

print(cnt)
for name in sorted(result):
    print(name)