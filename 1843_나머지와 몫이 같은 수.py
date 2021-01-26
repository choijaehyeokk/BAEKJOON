import sys
N = int(sys.stdin.readline().rstrip())
numbers: list = []
for i in range(1, N):
    numbers.append(i*N + i)
print(sum(numbers))