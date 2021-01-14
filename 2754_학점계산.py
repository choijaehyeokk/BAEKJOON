import sys

grade = sys.stdin.readline().rstrip()
score: float = 0
if grade[0] == 'F' :print(0.0)
else:
    if grade[0] == 'A': score = 4.0
    elif grade[0] == 'B': score = 3.0
    elif grade[0] == 'C': score = 2.0
    else: score = 1.0

    if grade[1] == '+':print(score + 0.3)
    elif grade[1] == '-':print(score - 0.3)
    else : print(score)