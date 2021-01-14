import sys

persons = list(map(int, sys.stdin.readline().split()))
persons = sorted(persons)
A = persons[3] + persons[0]
B = persons[1] + persons[2]

print(A - B if A > B else B - A)