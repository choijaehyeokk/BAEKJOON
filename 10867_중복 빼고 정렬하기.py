import sys
N = int(sys.stdin.readline().rstrip())
numbers = set(list(map(int, sys.stdin.readline().split())))
print(*sorted(numbers))