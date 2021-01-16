import sys

N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(1)
else:
    for i in range(29):
        if N % 2 != 0 or N == 2:
            break
        else:
            N = N // 2
    print(1 if N == 2 else 0)
