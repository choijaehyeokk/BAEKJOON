import sys
N = int(sys.stdin.readline().rstrip())
rows = []
for _ in range(N):
    rows.append(int(sys.stdin.readline().rstrip()))

rows = sorted(rows, reverse=True)
for i in range(N):
    rows[i] = rows[i] * (i+1)
print(max(rows))