import sys

K, L = map(int, sys.stdin.readline().split())
numbers = []
for i in range(2, K+1):
    if K % i == 0:
        K = K // i
        numbers.append(i)

minimum = min(numbers)
if L <= minimum: print("GOOD")
else: print("BAD {}".format(minimum))




