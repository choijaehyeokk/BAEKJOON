import sys

def GCD(a: int, b: int)->int:
    if a > b:
        a, b = b, a
    if b % a == 0: return a
    else: return GCD(a, b%a)

A, B = map(int, sys.stdin.readline().split())

result = GCD(A,B)
print(result)
print((A // result) * (B // result) * result)