import sys
N = int(sys.stdin.readline().rstrip())
names: list = []
player: dict = {}
for _ in range(N):
    names.append(sys.stdin.readline().rstrip())
for n in names:
    if not n[0] in player: player[n[0]] = 1
    else:player[n[0]] += 1
names.clear()
for k, v in player.items():
    if v >= 5: names.append(k)
if len(names) == 0 : print('PREDAJA')
else:
    names = sorted(names)
    for i in names:
        print(i, end='')

