# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:21:42 2022

@author: Samsung
"""

import random

def test1():
    data = [1,3,5,7]
    
    for i in range(4):
        a = data[i]
        print(a)
    print()

    for i in range(len(data)):
        a = data[i]
        print(a)
    print()
    
    for v in data:
        print(v)
    print()
    
    for i,v in enumerate(data):
        print(i,v)

test1()