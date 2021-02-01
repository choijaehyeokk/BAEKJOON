import sys
numbers = [0] * 10001
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    A = int(sys.stdin.readline().rstrip())
    numbers[A] += 1

for j in range(1, len(numbers)):
    if numbers[j] != 0:
        for k in range(numbers[j]):
            print(j)