import sys
N = int(sys.stdin.readline().rstrip())
numbers: list = []
for _ in range(N): numbers.append(int(sys.stdin.readline().rstrip()))
for s in sorted(numbers): print(s)
