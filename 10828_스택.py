import sys
N = int(sys.stdin.readline().rstrip())
stack = []
def push(n: int):
    global stack
    stack.append(n)

def top():
    global stack
    if not stack: print(-1)
    else: print(stack[len(stack)-1])

def size():
    global stack
    print(len(stack))

def empty():
    global stack
    print(1 if not stack else 0)

def pop():
    global stack
    if not stack: print(-1)
    else:
        print(stack[len(stack)-1])
        stack.pop(len(stack)-1)

for i in range(N):
    cmd = sys.stdin.readline().split()
    oprand = cmd[0]
    if oprand == 'push':
        push(cmd[1])
    elif oprand == 'top':
        top()
    elif oprand == 'size':
        size()
    elif oprand == 'pop':
        pop()
    elif oprand == 'empty':
        empty()
