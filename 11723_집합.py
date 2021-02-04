import sys

M = int(sys.stdin.readline().rstrip())
S = []
def add(s: list, n: str):
    if n in s: return
    else: s.append(n);

def remove(s: list, n: str):
    if n not in s: return
    else: s.remove(n); return

def check(s: list, n: str)->int:
    if n in s: return 1
    else: return 0

def toggle(s: list, n: str):
    if n in s: s.remove(n)
    else: s.append(n)

def all_set(s: list):
    s.clear()
    return ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

def empty(s: list):
    return []

for _ in range(M):
    commands = sys.stdin.readline().split()
    if len(commands) == 2:
        command = commands[0]
        num = commands[1]
    else:
        command = commands[0]
    if command == 'add':
        add(S, num)
    elif command == 'remove':
        remove(S, num)
    elif command == 'check':
        print(check(S, num))
    elif command == 'toggle':
        toggle(S, num)
    elif command == 'all':
        S = all_set(S)
    elif command == 'empty':
        S = empty(S)
    #print(S)