#!/urs/bin/python3
'''Module that creates the files for exercise'''


archives = ['0-subs.py', '1-top_ten.py', '2-recurse.py', '100-count.py']
text = '#!/usr/bin/python3'
for x in archives:
    with open(x, mode='w', encoding='utf-8') as f:
        i = 0
        i = f.write(text)
