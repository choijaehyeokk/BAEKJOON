import sys
numbers: list = []
for i in range(10):
    N = int(sys.stdin.readline().rstrip())
    numbers.append(N % 42)
print(len(set(numbers)))