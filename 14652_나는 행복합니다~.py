import sys

input_numbers = list(map(int, list(sys.stdin.readline().split())))

counter = 1
column = 0
flag = False
seat = input_numbers[2]

while flag != True:
    if seat < (input_numbers[1]*counter):
        row = counter
        break
    counter += 1

for x in range((row-1)*input_numbers[1], row*input_numbers[1]):
    if x == seat:
        print(row-1, column)
        break
    column += 1


