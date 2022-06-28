# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:00:10 2022

@author: Samsung
"""

import numpy as np
np.random.seed(24)

def test1():
    data = np.random.randint(0,10,(10,))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data[data > 5]
    print(data1, data1.shape)
    print(data > 5)
    print("-------------------------------------------------------")
    
    data2 = data[data == 7]
    print(data2, data2.shape)
    print("-------------------------------------------------------")
    
    data3 = data[data != 5]
    print(data3, data3.shape)
    print("-------------------------------------------------------")

# test1()

def test2():
    data = np.random.randint(0,10,(5,3))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data[data > 5]
    print(data1, data1.shape)
    print("-------------------------------------------------------")
    
    data2 = data[:,-1:] > 5
    print(data2, data.shape)
    print("-------------------------------------------------------")
    
    data3 = data[:,-1]
    print(data3, data3.shape)
    data4 = data3[data3 > 5]
    print(data4, data4.shape)
    
    
# test2()

def test3():
    data = np.random.randint(0,10,(10,))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = np.where(data>5,1,0)
    print(data1, data1.shape)
    print("-------------------------------------------------------")
    
test3()