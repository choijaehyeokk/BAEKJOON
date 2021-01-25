import sys

def is_complete(N: int):
    divisor: list = []
    flag: bool = False
    for i in range(1, N):
        if N % i == 0: divisor.append(i)
    if sum(divisor) == N: flag = True

    return divisor, flag

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == -1: break
    divisors, is_com = is_complete(N)
    if is_com:
        print('{0} = {1}'.format(N, ' + '.join(map(str,divisors))))
    else:
        print('{0} is NOT perfect.'.format(N))



