import sys
numbers = list(map(int, sys.stdin.readline().split()))
string = sys.stdin.readline().rstrip()

num_dic: dict = {}
numbers = sorted(numbers)
for n in range(3):
    if n == 0: num_dic['A'] = numbers[0]
    elif n == 1: num_dic['B'] = numbers[1]
    else: num_dic['C'] = numbers[2]
for i in range(3):
    print(num_dic[string[i]],end=' ')
