import sys

month = int(sys.stdin.readline().rstrip())
day = int(sys.stdin.readline().rstrip())

if month <= 2:
    if month == 2 and day == 18:
        print("Special")
    elif month == 1 or day < 18:
        print("Before")
    else:
        print("After")
else:
    print("After")