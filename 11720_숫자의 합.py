import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int,list(sys.stdin.readline().rstrip())))
result: int = 0
for i in range(N):
    result += numbers[i]
print(result)