import sys
T = int(sys.stdin.readline().rstrip())
first_contest = {'1' : 500, '3': 300, '6': 200, '10': 50, '15': 30, '21': 10}
second_contest = {'1' : 512, '3': 256, '7': 128, '15': 64, '31': 32}

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if (A > 21 or A == 0) and (B > 31 or B == 0): print(0); continue
    first_A, first_B = 1, 1
    result_A, result_B = 0, 0
    for i in range(1, len(first_contest)+1):
        if first_A >= A and A > 0: result_A = first_contest[str(first_A)]; break
        first_A += i+1

    for j in range(1, len(second_contest)+1):
        if first_B >= B and B > 0: result_B = second_contest[str(first_B)]; break
        first_B += pow(2, j)
    print((result_A + result_B)*10000)


'''
1차 페스티벌
1등	500만원	1명
2등	300만원	2명
3등	200만원	3명
4등	50만원	4명
5등	30만원	5명
6등	10만원	6명

2차 페스티벌
순위	상금	인원
1등	512만원	1명
2등	256만원	2명
3등	128만원	4명
4등	64만원	8명
5등	32만원	16명
'''