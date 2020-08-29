#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:17:19 2020

@author: linchiungying
"""


num=int(input("how many students?"))
scores=[]
for i in range(num):
    name=input('name?')
    score=(int(input('score?')))
    scores.append(name)
    scores.append(score)
    
highname='' 
highscore=0

for i in range(1,num*2,2):
    if scores[i]>highscore:
       highscore=scores[i]
       highname=scores[i-1]
       
lowname="" 
lowscore=101

for i in range(1,num*2,2):
    if scores[i]<lowscore:
       lowscore=scores[i]
       lowname=scores[i-1]