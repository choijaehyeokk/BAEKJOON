import sys, string, collections
N, B = map(int, sys.stdin.readline().split())
symbols: list = list(string.digits) + list(string.ascii_uppercase)
Base = collections.deque()
while N >= B:
    Base.appendleft(N % B)
    N = N // B
Base.appendleft(N)
for i in Base:
    print(symbols[i], end='')