import sys

numbers = list(map(int, list(sys.stdin.readline().split())))

if numbers[0] * numbers[1] > numbers[2]:
    print(numbers[0]*numbers[1]-numbers[2])
else:
    print(0)