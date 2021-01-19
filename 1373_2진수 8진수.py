import sys
binary = sys.stdin.readline().rstrip()
binary = int(binary, 2)
print(format(binary, 'o'))