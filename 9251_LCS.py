# import sys
# A = sys.stdin.readline().rstrip()
# B = sys.stdin.readline().rstrip()
#
# def lcs(a: str, b: str, m: int, n: int):
#     if m == 0 or n == 0:
#         return 0
#     elif a[m-1] == b[n-1]: return 1 + lcs(a, b, m-1, n-1)
#     else:
#         return max(lcs(a, b, m, n-1), lcs(a, b, m-1, n))
# print(lcs(A,B, len(A), len(B)))

import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    C = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0: C[i][j] = 0
            elif X[i - 1] == Y[j - 1]: C[i][j] = C[i - 1][j - 1] + 1
            else: C[i][j] = max(C[i - 1][j], C[i][j - 1])
    return C[m][n]

print(lcs(A,B))