'''
블래스터 라이플	$350.34
시각 센서	$230.90
청각 센서	$190.55
팔	$125.30
다리	$180.90
'''
import sys

test_case = int(sys.stdin.readline().rstrip())
prices = {'blaster' : 350.34, 'sight' : 230.90, 'hear': 190.55,'arm':125.30, 'leg':180.90}
for i in range(test_case):
    A, B, C, D, E = map(int, sys.stdin.readline().split())
    print('$%.2f' %(prices['blaster']*A+ prices['sight'] *B+prices['hear']*C + prices['arm']*D + prices['leg']*E))