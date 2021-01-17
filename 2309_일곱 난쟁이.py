import sys
Dwarf: list = []
for i in range(9):
    N = int(sys.stdin.readline().rstrip())
    Dwarf.append(N)
Dwarf = sorted(Dwarf)

for a in range(len(Dwarf)-6):
    for b in range(a+1, len(Dwarf)-5):
        for c in range(b+1, len(Dwarf)-4):
            for d in range(c+1, len(Dwarf)-3):
                for e in range(d+1, len(Dwarf)-2):
                    for f in range(e+1, len(Dwarf)-1):
                        for g in range(f+1, len(Dwarf)):
                            if Dwarf[a] + Dwarf[b] + Dwarf[c] +Dwarf[d] + Dwarf[e] + Dwarf[f] +Dwarf[g] == 100:
                                print(Dwarf[a])
                                print(Dwarf[b])
                                print(Dwarf[c])
                                print(Dwarf[d])
                                print(Dwarf[e])
                                print(Dwarf[f])
                                print(Dwarf[g])
                                exit()

