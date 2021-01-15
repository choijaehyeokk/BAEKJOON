import sys
max_person: int = 0
current_person: int = 0
for i in range(10):
    out_person, in_person = map(int,sys.stdin.readline().split())
    current_person -= out_person
    current_person += in_person
    if current_person > max_person: max_person = current_person
print(max_person)