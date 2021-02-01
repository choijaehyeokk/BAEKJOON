import sys
N = int(sys.stdin.readline().rstrip())
points = []
for _ in range(N):
    points.append(list(map(int ,sys.stdin.readline().split())))
points.sort(key=lambda x:(x[0], x[1]))

for x, y in points:
    print(x, y)