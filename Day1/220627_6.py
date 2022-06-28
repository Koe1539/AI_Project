# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:46:04 2022

@author: Samsung
"""
import numpy as np
np.random.seed(24)

def test1():
    data = np.random.randint(0,10,(2,5))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data.T
    print(data1, data1.shape)
    print("-------------------------------------------------------")

test1()