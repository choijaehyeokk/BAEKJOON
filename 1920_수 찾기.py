import sys
N = int(sys.stdin.readline().rstrip())
n_numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
m_numbers = list(map(int, sys.stdin.readline().split()))
n_numbers = sorted(n_numbers)

for n in m_numbers:
    center = len(n_numbers)//2
    i, j = 0, len(n_numbers) - 1
    flag = False
    while i < j:
        if n_numbers[i] == n or n_numbers[j] == n or n_numbers[center] == n:
            flag = True
            break

        if n > n_numbers[center]:
            i = center + 1
        elif n < n_numbers[center]:
            j = center - 1
        center = (i + j) // 2
    print(1 if flag else 0)

