import sys
from decimal import *
N = str(Decimal(1/2**(int(sys.stdin.readline().rstrip()))))
if 'E' in N:
    number = N.split('E-')
    number[0] = ''.join(number[0].split('.'))
    print('0.', end='')
    print('0' * (int(number[1]) - 1) + number[0])
else: print(N)
