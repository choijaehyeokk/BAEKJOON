import sys
idx = 1
while True:
    L, P, V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and  V == 0:
        break

    if V % P <= L:
        print("Case {}: {}".format(idx, (V // P) * L + (V % P)))
    else:
        print("Case {}: {}".format(idx, (V // P) * L + L))
    idx += 1