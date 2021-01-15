import sys
N = int(sys.stdin.readline().rstrip())
result: int = 0
for i in range(N):
    student, apple = map(int, sys.stdin.readline().split())
    result += apple % student
print(result)