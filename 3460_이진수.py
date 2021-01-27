import sys

test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    N = int(sys.stdin.readline().rstrip())

    bin_number = format(N, 'b')
    length = len(bin_number)
    for i in range(length-1, -1, -1):
        if bin_number[i] == '1':
            if i == 0: print(length-i-1)
            else: print(length-i-1, end=' ')

