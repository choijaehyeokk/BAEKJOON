import sys, math

width = int(sys.stdin.readline().rstrip())
r = int(sys.stdin.readline().rstrip())
print(width * 2  + (2 * math.pi * r))