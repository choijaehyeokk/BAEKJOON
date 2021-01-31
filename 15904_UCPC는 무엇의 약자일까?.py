import sys
string = list(sys.stdin.readline())
words = ""
flag = False
for i in range(len(string)):
    if string[i].isupper() and (string[i] =='U' or string[i] == 'C' or string[i] == 'P'):
        words += string[i][0]
for a in range(len(words)-3):
    if words[a] == 'U':
        for b in range(a+1, len(words)-2):
            if words[b] == 'C':
                for c in range(b+1, len(words)-1):
                    if words[c] == 'P':
                        for d in range(c+1, len(words)):
                            if words[d] == 'C':
                                flag = True
print('I love UCPC' if flag == True else 'I hate UCPC')
