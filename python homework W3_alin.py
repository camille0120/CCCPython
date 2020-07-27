#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:39:02 2020

@author: camillelin
"""

a=[]
b=input("班上共有多少人?")
for i in range(int(b)):
    score=int(input("score?"))
    a.append(score)
    
t=0
for i in a:
    t=t+i
        
print("average=",t//int(b))
