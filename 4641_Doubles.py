import sys
while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers[0] == -1: break

    count: int = 0
    length = len(numbers)

    for i in range(length):
        if numbers[i] == 0: break
        A = numbers[i] / 2
        for j in range(length):
            if A == numbers[j]:
                count += 1
    print(count)