import sys

DHM = list(map(int, list(sys.stdin.readline().split())))
result : int = 0
result = (DHM[0]- 11) * 1440 + (DHM[1]- 11) * 60 + (DHM[2] - 11)
print(-1 if result < 0 else result)