import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
print("{0} {1}".format(min(numbers),max(numbers)))