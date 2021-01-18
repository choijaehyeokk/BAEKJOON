import sys
money = int(sys.stdin.readline().rstrip())
money = 1000 - money
money_list: list = [500, 100, 50, 10, 5, 1]
result: list = []
for i in range(len(money_list)):
    result.append(money // money_list[i])
    money -= money_list[i] * result[i]
print(sum(result))

