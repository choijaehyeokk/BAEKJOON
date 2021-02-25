import sys
N = int(sys.stdin.readline().rstrip())
numbers = []
while N > 1:
    for i in range(2, N+1):
        if N % i == 0:
            N = N // i
            numbers.append(i)
            break
for N in numbers:
    print(N)