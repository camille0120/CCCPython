#!/usr/bin/env python3
import random
a=random.randint(1,10)

b=input("guess(1-10)")
c=int(b)
if a==c :
    print("right")
else:
    print("wrong")


