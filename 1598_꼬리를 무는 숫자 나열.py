import sys

X, Y = map(int, sys.stdin.readline().split())
if X % 4 == 0 and Y % 4 != 0:
    X -= 1
    X_axis = abs((X % 4) - (Y % 4))
    Y_axis = abs((X // 4) - (Y // 4))
    print(X_axis + Y_axis + 1)
elif Y % 4 == 0 and X % 4 != 0:
    Y -= 1
    X_axis = abs((X % 4) - (Y % 4))
    Y_axis = abs((X // 4) - (Y // 4))
    print(X_axis + Y_axis + 1)
else:
    X_axis = abs((X % 4) - (Y % 4))
    Y_axis = abs((X // 4) - (Y // 4))
    print(X_axis + Y_axis)







