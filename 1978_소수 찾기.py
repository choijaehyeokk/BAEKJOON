import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0
def is_div(n: int)->bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    elif is_div(numbers[i]): cnt += 1
print(cnt)