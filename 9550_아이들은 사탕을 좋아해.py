import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N, K = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    students: int = 0
    if K > max(numbers):
        print(0)
        continue

    for j in numbers:
        students += j // K
    print(students)

