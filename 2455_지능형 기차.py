import sys
max_number, person = 0, 0
for i in range(4):
    out_person, in_person = map(int, sys.stdin.readline().split())
    person -= out_person
    person += in_person
    if max_number < person: max_number = person
print(max_number)


