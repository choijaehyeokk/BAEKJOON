import sys
T, L = map(int, sys.stdin.readline().split())
input_dnas = []
dnas = []
result = ''
cnt = 0
for _ in range(T):
    input_dnas.append(sys.stdin.readline().rstrip())

for i in range(L):
    temp = {}
    for j in input_dnas:
        if j[i] not in temp:
            temp[j[i]] = 1
        else:
            temp[j[i]] += 1
    max_value = max(temp.values())
    cnt += (T - max_value)
    for k, v in list(temp.items()):
        if temp[k] != max_value:
            temp.pop(k)
    dnas.append(list(temp))

for j in range(L):
    result += sorted(dnas[j])[0]

print(result)
print(cnt)