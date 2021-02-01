import sys
N = list(sys.stdin.readline().rstrip())
N = sorted(N,reverse=True)
print(int(''.join(N)))