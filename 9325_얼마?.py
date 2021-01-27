import sys
test_case = int(sys.stdin.readline().rstrip())
for i in range(test_case):
    carprice = int(sys.stdin.readline().rstrip())
    options = int(sys.stdin.readline().rstrip())

    while options:
        p , q = map(int, sys.stdin.readline().split())
        carprice += p*q
        options-=1
    print(carprice)

