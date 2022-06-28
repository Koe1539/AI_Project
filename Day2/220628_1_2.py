# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:17:50 2022

@author: Samsung
"""

import random

def test1():
    x = [[0,0],[0,1],[1,0],[1,1]]
    y = [0,1,1,1]
    
    # system parameter = 시스템에서 정의한 값
    # hyper parameter = 사람이 정의한 값
    w = [random.random(),random.random(),random.random()]
    for epoch in range(50):
        print(epoch,"-----------------------------------------------")
        for i in range(len(x)):
            net = x[i][0] * w[0] + x[i][1] * w[1] + 1 * w[2]
            
            if net > 0:
                act = 1
            else:
                act = 0
                
            loss = y[i] - act
            
            w[0] = w[0] + 0.01 * loss * x[i][0]
            w[1] = w[1] + 0.01 * loss * x[i][1]
            w[2] = w[2] + 0.01 * loss * 1
            
            print(x[i], act, y[i])
    
test1()