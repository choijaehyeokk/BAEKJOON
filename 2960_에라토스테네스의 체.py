import sys

def prime_list(n: int):
    sieve = [True] * (n+1)
    cnt = 0
    for i in range(2, len(sieve) + 1):
        for j in range(i, N + 1, i):
            if sieve[j] == True:
                sieve[j] = False
                cnt = cnt + 1
                if cnt == K:
                    return j

N, K = map(int, sys.stdin.readline().split())
print(prime_list(N))
