import sys
C, K, P = map(int, sys.stdin.readline().split())
total_wine: int = 0
for i in range(C+1):
    total_wine += (K*i + P*(pow(i, 2)))
print(total_wine)