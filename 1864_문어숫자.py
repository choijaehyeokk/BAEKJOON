import sys

octo = {'-':0,
        "\\":1,
        '(': 2,
        '@': 3,
        '?': 4,
        '>': 5,
        '&': 6,
        '%': 7,
        '/': -1}
while True:
    number = sys.stdin.readline().rstrip()
    if number == '#' : break
    result : int = 0
    squared = len(number) - 1
    for i in range(len(number)):
        result += octo[number[i]] * pow(8, squared)
        squared -= 1
    print(result)

