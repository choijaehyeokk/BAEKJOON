import sys

number = int(sys.stdin.readline().rstrip())

if number == 0:
    print("divide by zero")
else:
    numbers = list(map(int, list(sys.stdin.readline().split())))

    if sum(numbers) == 0:
        print('divide by zero')
    else:
        print('1.00')