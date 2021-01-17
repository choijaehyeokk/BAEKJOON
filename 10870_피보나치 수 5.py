import sys
N = int(sys.stdin.readline().rstrip())
def fibo(n: int)-> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(N))

#피보나치 by recursive