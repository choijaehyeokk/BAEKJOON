import sys

a, b = map(int, sys.stdin.readline().split())
n_max = max(a, b)
n_min = min(a, b)
n = n_max - n_min
s = (n * (n + 1)) // 2
print(s + (n_min * (n + 1)))