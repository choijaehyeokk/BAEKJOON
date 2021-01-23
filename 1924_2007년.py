import sys
month, day = map(int, sys.stdin.readline().split())
months = {'1': 31, '2':28,'3':31,'4':30, '5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
DoW = ['SUN','MON','TUE','WED','THU','FRI','SAT']
before_m: int = 0
for k, v in months.items():
    if k == str(month): break
    before_m += v
print(DoW[(before_m+day)%7])