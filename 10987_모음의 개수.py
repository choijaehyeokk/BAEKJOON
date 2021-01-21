import sys
string = sys.stdin.readline().rstrip()
result: int = 0
for i in string:
    if i == 'a' or i == 'o' or i =='e' or i=='u' or i=='i': result +=1
print(result)