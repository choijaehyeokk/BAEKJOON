import sys

shack = sys.stdin.readline().rstrip()
pointer: int = 0
for i in range(len(shack)):
    rule = shack[i]
    if rule == 'A':
        if pointer == 0 : pointer = 1
        elif pointer == 1 : pointer = 0
    elif rule == 'B':
        if pointer == 1 : pointer = 2
        elif pointer == 2: pointer = 1
    elif rule == 'C':
        if pointer == 0 : pointer = 2
        elif pointer == 2 : pointer = 0
print(pointer+1)