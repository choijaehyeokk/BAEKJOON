import sys

number = sys.stdin.readline().rstrip()

for i in range(len(number)):
    number = int(number[0]) * len(number)
    number = str(number)

if len(number) == 1:
    print("FA")
else:
    print("NFA")

