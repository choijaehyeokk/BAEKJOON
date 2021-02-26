import sys,collections
while True:
    string = sys.stdin.readline().rstrip()
    flag = True
    if len(string) == 1 and string == '.':
            break
    else:
        symbol = collections.deque()
        stack = []
        for i in range(len(string)):
            if string[i] == '(': symbol.append('(')
            elif string[i] == ')': symbol.append(')')
            elif string[i] == '[': symbol.append('[')
            elif string[i] == ']': symbol.append(']')

        if not symbol: print('yes')
        else:
            while symbol:
                n = symbol.popleft()
                if n == ')':
                    if stack:
                        m = stack.pop()
                        if m != '(':
                            flag = False
                            break
                    else:
                        flag = False
                        break
                elif n == ']':
                    if stack:
                        m = stack.pop()
                        if m != '[':
                            flag = False
                            break
                    else:
                        flag = False
                        break
                else:
                    stack.append(n)

            if stack or flag == False: print('no')
            else: print('yes')