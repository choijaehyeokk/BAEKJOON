import sys

N = int(sys.stdin.readline().rstrip())
print(pow((2*pow(2, N-1)+1), 2))