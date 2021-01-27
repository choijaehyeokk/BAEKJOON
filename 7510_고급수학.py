import sys, math

test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    numbers = sorted(list(map(int, sys.stdin.readline().split())))
    if numbers[2] == math.sqrt(pow(numbers[0],2) + pow(numbers[1],2)): print('Scenario #{0}:\nyes'.format(i+1))
    else: print('Scenario #{0}:\nno'.format(i+1))
    if i != test_case-1: print('')
