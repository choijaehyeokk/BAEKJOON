import sys
N = int(sys.stdin.readline().rstrip())
number = list(str(bin(N))[2:])
print(number.count('1'))