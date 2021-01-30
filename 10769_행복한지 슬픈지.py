import sys
emo = {'happy': 0, 'sad': 0}
string = sys.stdin.readline().rstrip()

for i in range(len(string)-2):
    if string[i:i+3] == ':-)':
        emo['happy'] += 1
    if string[i:i+3] == ':-(':
        emo['sad'] += 1
if emo['happy'] == emo['sad'] == 0: print('none')
elif emo['happy'] > emo['sad']: print('happy')
elif emo['happy'] < emo['sad']: print('sad')
else:
    print('unsure')
