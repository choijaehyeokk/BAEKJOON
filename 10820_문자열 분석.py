# import sys
#
# while True:
#     try:
#         string = sys.stdin.readline().rstrip()
#     except EOFError:
#         break
#     if len(string) == 0: break
#     small, big, num, space = 0, 0, 0, 0
#     for i in string:
#         if i == ' ': space+=1
#         elif i.isupper(): big+=1
#         elif i.islower(): small+=1
#         elif i >= '0' and i <= '9' : num+=1
#         else: break
#     print(small, big, num, space)
#

import sys

while True:
    string = sys.stdin.readline().rstrip('\n')

    if not string:
        break
    small, big, num, space = 0, 0, 0, 0
    for each in string:
        if each.islower():
            small += 1
        elif each.isupper():
            big += 1
        elif each.isdigit():
            num += 1
        elif each.isspace():
            space += 1

    print(small, big, num, space)