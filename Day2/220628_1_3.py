# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:19:47 2022

@author: Samsung
"""

import numpy as np

def test1():
    # input: 3, hidden: 6, output: 1
    x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]]) # (4,3)
    y = np.array([[0],[1],[1],[0]]) # (4,1)
    print(x.shape, y.shape)
    print("-----------------------------------------------------------")
    
    weight0 = np.random.random((3,6)) # (3,6)
    print(weight0.shape)
    weight1 = np.random.random((6,1)) # (6,1)
    print(weight1.shape)
    print("-----------------------------------------------------------")
    
    for i in range(5000):
        # 전방향 계산
        net1 = x @ weight0 # (4,3) @ (3,6) = (4,6)
        print(net1.shape)
        act1 = 1 / (1 + np.exp(-net1)) # (4,6)
        print(act1.shape)
        act1[:,-1] = 1.0
        print("-----------------------------------------------------------")
        
        net2 = act1 @ weight1 # (4,6) @ (6,1) = (4,1)
        print(net2.shape)
        act2 = 1 / (1 + np.exp(-net2)) # (4,1)
        print(act2.shape)
        print("-----------------------------------------------------------")
        
        act2_error = act2 - y # (4,1) - (4,1) = (4,1)
        t = act2 * (1 - act2) # (4,1) * (1 - (4,1)) = (4,1)
        act2_delt = act2_error * t # (4,1)
        print(act2_delt.shape)
        print("-----------------------------------------------------------")
        
        weight1 = weight1 - 0.2 * (act1.T @ act2_delt) # (6,4) @ (4,1) = (6,1)
        
        act1_error = act2_delt @ weight1.T # (4,1) @ (1,6) = (4,6)
        t = act1 * (1 - act1) # (4,6) * (1 - (4,6)) = (4,6)
        act1_delt = act1_error * t # (4,6) * (4,6) = (4,6)
        weight0 = weight0 - 0.2 * (x.T @ act1_delt) # (3,4) @ (4,6) = (3,6)
        
        print(x)
        print(y)
        print(act2)

test1()