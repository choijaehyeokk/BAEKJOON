import sys
N = int(sys.stdin.readline().rstrip())
n_nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
m_nums = list(map(int, sys.stdin.readline().split()))
results = []
n_nums = sorted(n_nums)

def binary_search(a: int)->bool:
    global n_nums
    i = 0
    j = len(n_nums)-1
    k = (i+j) // 2
    while i <= j:
        if n_nums[k] == a:
            return True
        elif n_nums[k] <= a:
            i = k+1
        else:
            j = k-1

        k = (i+j) // 2
    return False

for A in range(len(m_nums)):
    if binary_search(m_nums[A]):
        results.append(1)
    else:
        results.append(0)
print(*results)