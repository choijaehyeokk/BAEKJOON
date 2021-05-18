import sys

input_string = list(sys.stdin.readline().rstrip())
sticks = 0
cnt = 0
index = 0
while index != len(input_string):
    if input_string[index] == '(':
        sticks += 1
        if input_string[index+1] == ')':
            index += 1
            sticks -= 1
            cnt += sticks
    else:
        sticks -= 1
        cnt += 1
    index+=1

print(cnt)