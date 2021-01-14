import sys

number = int(sys.stdin.readline().rstrip())

for i in range(number):
    price : float = 0
    price = float(sys.stdin.readline().rstrip())
    price *= 0.8

    print("$%0.2f" %price)
    #print("${0:0.2f}".format(price))

