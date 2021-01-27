import sys

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0: break
    numbers = sorted(numbers)
    if numbers[2] - numbers[1] == numbers[1] - numbers[0] and numbers[2] -numbers[1] != 0: print('AP {0}'.format(2*numbers[2] - numbers[1]))
    elif numbers[2] // numbers[1] == numbers[1] // numbers[0] and numbers[2] // numbers[1] != 0: print('GP {0}'.format(numbers[2]*(numbers[2]//numbers[1])))