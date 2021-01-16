import sys
answer: int = 1
numbers: dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in range(3):
    num = int(sys.stdin.readline().rstrip())
    answer *= num
for j in str(answer):
    numbers[j] += 1
for k, v in numbers.items():
    print(v)
