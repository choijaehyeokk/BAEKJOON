import sys, decimal

N = int(sys.stdin.readline().rstrip())

n = str(float(1/pow(2, N)))
if 'e' in n:
    n = n.split('e-')
    number = n[0].split('.')
    print('0.' + int(n[1])*'0' + number[0] + number[1])
else:
    print(n)

