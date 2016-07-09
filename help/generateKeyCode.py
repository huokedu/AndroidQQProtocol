# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:35:53 2016
@author: Alost
"""

if __name__ == '__main__':
    keys = [('', '')]
    with open('keys.log') as f:
        lines = f.readlines()
        lines = [li.strip() for li in lines]
        for i in xrange(0, len(lines), 2):
            keys.append((lines[i][len('pubKey: '):], lines[i+1][len('shareKey: '):]))

    #generate java code
    with open('keys_code.java', 'w') as f:
        for key in keys:
            f.write('pubKeys.add("' + key[0] + '");\n')
            f.write('shareKeys.add("' + key[1] + '");\n')

    #generate python code
    with open('keys_code.py', 'w') as f:
        for key in keys[1:]:
            f.write('pubKeys.append("' + key[0] + '");\n')
            f.write('shareKeys.append("' + key[1] + '");\n')