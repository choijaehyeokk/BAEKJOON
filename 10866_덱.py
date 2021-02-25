import sys, collections

N = int(sys.stdin.readline().rstrip())
deque = collections.deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.appendleft(command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    else:
        if command[0] == 'pop_front':
            if deque:
                A = deque.popleft()
                print(A)
            else:
                print(-1)
        elif command[0] == 'pop_back':
            if deque:
                A = deque.pop()
                print(A)
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(deque))
        elif command[0] == 'empty':
            if deque:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if deque:
                print(deque[len(deque)-1])
            else:
                print(-1)
