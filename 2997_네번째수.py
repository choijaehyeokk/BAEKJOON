import sys

numbers = sorted(list(map(int, sys.stdin.readline().split())))
if numbers[1] - numbers[0] == numbers[2] - numbers[1] : print(2*numbers[2]-numbers[1])
else:
    if numbers[1] - 2*(numbers[2] - numbers[1]) == numbers[0]:print(2*numbers[1] - numbers[2])
    else: print(numbers[0]+numbers[2]-numbers[1])


# for i in range(-100, 101):
#     numbers.append(i)
#     numbers = sorted(numbers)
#     if 4*(numbers[0]+numbers[3]) / 2 == sum(numbers):
#          print(i)
#          break
#     else:
#          numbers.remove(i)