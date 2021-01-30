import sys
N = int(sys.stdin.readline().rstrip())
# 별 : 4, 동그라미 : 3, 네모 : 2, 세모 : 1
A_dic, B_dic = {'1':0, '2':0, '3':0, '4':0}, {'1':0, '2':0, '3':0, '4':0}
for _ in range(N):
    A = sys.stdin.readline().split()
    B = sys.stdin.readline().split()

    for i in range(1, int(A[0])+1):
        A_dic[A[i]] += 1
    for i in range(1, int(B[0])+1):
        B_dic[B[i]] += 1

    if A_dic['4'] != B_dic['4']:
        print('A' if A_dic['4'] > B_dic['4'] else 'B')
    elif A_dic['3'] != B_dic['3']:
        print('A' if A_dic['3'] > B_dic['3'] else 'B')
    elif A_dic['2'] != B_dic['2']:
        print('A' if A_dic['2'] > B_dic['2'] else 'B')
    elif A_dic['1'] != B_dic['1']:
        print('A' if A_dic['1'] > B_dic['1'] else 'B')
    else:
        print('D')
    A_dic, B_dic = {'1': 0, '2': 0, '3': 0, '4': 0}, {'1': 0, '2': 0, '3': 0, '4': 0}

