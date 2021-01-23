import sys
N, K = map(int, sys.stdin.readline().split())
def factorial(A: int)->int:
    result: int = 1
    for i in range(1, A+1): result *= i
    return result
print(int(factorial(N)/(factorial(N-K)*factorial(K))))