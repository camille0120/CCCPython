#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:39:02 2020

@author: camillelin
"""

scores=[]
num=input("班上共有多少人?")
for i in range(int(num)):
    score=int(input("score?"))
    scores.append(score)
    
t=0
for i in scores:
    t=t+i
 
high = 0
for each_score in scores:
    if each_score>high:
        high=each_score
    
    
low = 100
for each_score in scores:
    if each_score<low:
        low=each_score
        
print("average=",t//int(num))
print("最高分為",high)
print("最低分為",low)
