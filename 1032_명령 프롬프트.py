import sys

N = int(sys.stdin.readline().rstrip())
result: list = list(sys.stdin.readline().rstrip())
length: int = len(result)
for _ in range(N-1):
    command = list(sys.stdin.readline().rstrip())
    for i in range(length):
        if result[i] != command[i]: result[i] = '?'
print(''.join(result))