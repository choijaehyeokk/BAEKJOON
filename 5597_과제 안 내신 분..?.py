import sys

students: list = [0] * 30
for i in range(28):
    x = int(sys.stdin.readline().rstrip())
    students[x-1] += 1

for j in range(30):
    if students[j] == 0:
        print(j+1)