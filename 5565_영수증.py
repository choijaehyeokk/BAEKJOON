import sys

total_price = int(sys.stdin.readline().rstrip())
for i in range(9):
    price = int(sys.stdin.readline().rstrip())
    total_price -= price
print(total_price)
