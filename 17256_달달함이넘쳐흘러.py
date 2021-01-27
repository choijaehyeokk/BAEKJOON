import sys

numbers_a= list(map(int, list(sys.stdin.readline().split())))
numbers_c = list(map(int, list(sys.stdin.readline().split())))

print(numbers_c[0] - numbers_a[2] , int(numbers_c[1] / numbers_a[1]) , numbers_c[2] - numbers_a[0])

