#!/urs/bin/python3
'''Module that creates the files for exercise'''


archives = ['0', '1', '2', '100']
text = '#!/usr/bin/python3'
for x in archives:
    with open('{}-main.py'.format(x), mode='w', encoding='utf-8') as f:
        i = 0
        i = f.write(text)
