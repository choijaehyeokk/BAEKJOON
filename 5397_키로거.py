import sys

TestCase = int(sys.stdin.readline().rstrip())
for _ in range(TestCase):
    string = list(sys.stdin.readline().rstrip())
    left_stack, right_stack = [], []

    for char in string:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack)) 