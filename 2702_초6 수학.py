import sys

def GCD(a: int, b: int)->int:
    if a < b:
        a, b = b, a

    if a % b == 0: return b
    else: return GCD(b, a - b)

def LCM(a: int, b: int, r: int)->int:
    result = (a // r) * (b // r) * r
    return result

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = GCD(a,b)
    print(LCM(a,b, result), result)