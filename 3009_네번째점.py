import sys
points_X: dict = {}
points_Y: dict = {}
for i in range(3):
    X, Y = map(int, sys.stdin.readline().split())
    if X in points_X: points_X[X] += 1
    else: points_X[X] = 1
    if Y in points_Y: points_Y[Y] += 1
    else: points_Y[Y] = 1
print([k for k, v in points_X.items() if 1 == v][0], [k for k, v in points_Y.items() if 1 == v][0])