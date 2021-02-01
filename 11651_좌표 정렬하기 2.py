import sys
N = int(sys.stdin.readline().rstrip())
points = []
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    points.append([X,Y])
points = sorted(points, key=lambda x:(x[1], x[0]))
for p in points:
    print(p[0], p[1])