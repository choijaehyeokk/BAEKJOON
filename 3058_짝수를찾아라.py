import sys

test_case = int(sys.stdin.readline().rstrip())
result: int = 0
min_number: int = 0
flag: bool = True
for i in range(test_case):
    numbers = sorted(list(map(int, sys.stdin.readline().split())))

    for i in range(7):
        if numbers[i] % 2 == 0 :
            result += numbers[i]
            if flag == True:
                min_number = numbers[i]
                flag = False

    print(result, min_number)
    result, flag = 0, True

