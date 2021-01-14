import sys

binary = sys.stdin.readline().rstrip()
result = int(binary, 2)*17
print(format(result, 'b'))

