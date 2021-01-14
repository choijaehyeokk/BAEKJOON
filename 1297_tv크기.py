'''
대각선의 길이와 높이, 너비 순으로 비율이 정해질때,
실제 높이와, 너비를 출력하라
'''
import sys, math

input_numbers = list(map(int, sys.stdin.readline().split()))

i = input_numbers[0] / math.sqrt(pow(input_numbers[1], 2) + pow(input_numbers[2], 2))
print(int(i*input_numbers[1]), int(i*input_numbers[2]))


