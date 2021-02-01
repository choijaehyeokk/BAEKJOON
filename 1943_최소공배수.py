import sys
N = int(sys.stdin.readline().rstrip())
def GCD(a: int, b: int)->int:
    if a > b:
        a, b = b, a
    if b % a == 0: return a
    else:
        return GCD(a, b % a)

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    result = GCD(A,B)
    print((A // result) * (B // result) * result)