import sys

for i in range(3):
    N = int(sys.stdin.readline().rstrip())
    numbers = []
    for i in range(N):
        number = int(sys.stdin.readline().rstrip())
        numbers.append(number)
    if sum(numbers) == 0 : print("0")
    elif sum(numbers) < 0 :print("-")
    else: print("+")
