import sys
number = list(map(int, sys.stdin.readline().rstrip()))
result = -1
sets = {'0': 0, '1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8':0,'9': 0}
for i in range(10):
    sets[str(i)] = number.count(i)

if (sets['6'] + sets['9']) % 2 == 0:
    sets['6'] = (sets['6'] + sets['9'])//2
else:
    sets['6'] = (sets['6'] + sets['9'])//2 + 1
sets['9'] = 0

for v in sets.values():
    if result < v:
        result = v
print(result)