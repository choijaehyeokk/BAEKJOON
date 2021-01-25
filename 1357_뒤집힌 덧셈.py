import sys
X, Y = map(int, sys.stdin.readline().split())
def Rev(n):
    n = int(str(n)[::-1])
    return n
print(Rev(Rev(X) + Rev(Y)))