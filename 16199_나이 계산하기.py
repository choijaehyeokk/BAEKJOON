import sys

birth_day = list(map(int, sys.stdin.readline().split()))
current_day = list(map(int, sys.stdin.readline().split()))

man_age : int = 0
year_age : int = current_day[0] - birth_day[0]
sae_age : int = year_age + 1

if current_day[1] > birth_day[1] or (current_day[1] == birth_day[1] and current_day[2]  >= birth_day[2]):
    man_age = sae_age -1
else:
    man_age = sae_age - 2

print(man_age)
print(sae_age)
print(year_age)

