import sys

money = int(sys.stdin.readline().split()[0])

print(int(money*0.78), int(((money - (money * 0.2) * 0.22))))