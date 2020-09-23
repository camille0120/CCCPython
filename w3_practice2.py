#!/usr/bin/env python3
a=[82, 1998, 74, 1990, 56, 'ww','qweq', 'stop','www','qwe']
b=[]
for i in a:
    if i=='stop':
        break
    elif type(i)==str:
        continue
    elif type(i)==int:
        if i<=109:
            b.append(i+1911)

        else:
            b.append(i)

