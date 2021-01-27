import sys
count = int(sys.stdin.readline().rstrip())
x : int = 1
y : int = count*2-2
for i in range(count -1):
    print(x * "*" + y *' ' + x *"*")
    y -= 2
    x += 1
print("*" * (2*count))
x -= 1
y += 2
for i in range(count -1):
    print(x * "*" + y * ' ' + x * "*")
    y += 2
    x -= 1