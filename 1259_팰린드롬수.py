import sys
while True:
    number = sys.stdin.readline().rstrip()
    if number == '0': break
    number = list(number)
    print('yes' if number == number[::-1] else 'no')
