import sys

test_case = int(sys.stdin.readline().rstrip())
numbers: list = []
for i in range(test_case):
    space = input()
    numbers.clear()
    N = int(sys.stdin.readline().rstrip())
    for j in range(N):
        number = int(sys.stdin.readline().rstrip())
        numbers.append(number)

    if sum(numbers) % N == 0:print('YES')
    else: print('NO')
