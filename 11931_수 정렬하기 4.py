import sys
N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
for x in sorted(numbers, reverse=True):
    print(x)