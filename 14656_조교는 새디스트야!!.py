import sys
N = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().split()))
count: int = 0
for i in range(N):
    if i+1 != students[i]: count += 1
print(count)