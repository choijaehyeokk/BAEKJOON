import sys

number = []
for i in range(4):
    A = int(sys.stdin.readline().rstrip())
    number.append(A)

if (number[0] == 8 or number[0] == 9) and (number[3] == 8 or number[3] == 9) and (number[1] == number[2]):
    print("ignore")
else:
    print("answer")