import sys
i, j, k = 1, 1, 1
year: int = 1
e, s, m = map(int,sys.stdin.readline().split())

while True:
    if e == i and s == j and m == k: break
    i ,j, k = i+1, j+1, k+1
    if i == 16: i = 1
    if j == 29: j = 1
    if k == 20: k = 1
    year += 1

print(year)