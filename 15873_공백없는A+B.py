import sys

numbers = sys.stdin.readline().rstrip()

if len(numbers) < 3:
    print(int(numbers[0]) + int(numbers[1]))
elif len(numbers) == 4:
    print(20)
else:
    for i in range(3):
        if numbers[i] == '0':
            print(10 + int(numbers[i-2]))
