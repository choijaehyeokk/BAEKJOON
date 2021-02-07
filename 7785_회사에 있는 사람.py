import sys
N = int(sys.stdin.readline().rstrip())
persons = {}
for _ in range(N):
    input_string = sys.stdin.readline().split()
    name = input_string[0]
    e_or_l = input_string[1]

    if e_or_l == 'enter':
        if name not in persons:
            persons[name] = True
    elif e_or_l == 'leave':
        persons.pop(name)

persons = sorted(persons, reverse=True)
for name in persons:
    print(name)