import sys
N = int(sys.stdin.readline().rstrip())
result: dict = {'zero': 0, 'one': 0}
for i in range(N):
    zero_one = int(sys.stdin.readline().rstrip())
    if zero_one == 0: result['zero'] += 1
    else: result['one'] += 1
print('Junhee is not cute!' if result['zero'] > result['one'] else 'Junhee is cute!')