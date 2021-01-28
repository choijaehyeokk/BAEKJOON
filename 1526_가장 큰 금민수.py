import sys
N = int(sys.stdin.readline().rstrip())
flag = False
for i in range(N, 3, -1):
    n = str(i)
    for j in range(len(n)):
        if n[j] != '4' and n[j] != '7': break
        if j == len(n)-1 and (n[j] == '4' or n[j] == '7'):
            flag = True
    if flag == True: print(i); break