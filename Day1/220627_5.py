# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:14:12 2022

@author: Samsung
"""
import numpy as np
np.random.seed(2022)
def test1():
    data1 = np.random.randint(0,10,(3,4))
    print(data1, data1.shape)
    
    data2 = np.random.randint(10,20,(4,5))
    print(data1, data2.shape)
    
    data3 = data1 @ data2 # (3,4)@(4,5)= (3,5)
    print(data3, data3.shape)
    
    data4 = np.dot(data1, data2)
    print(data4, data4.shape)
    
# test1()

def test2():
    data1 = np.random.randint(0,100,(5,4))
    print(data1, data1.shape)
    
    data2 = data1[:,[0,1]]
    print(data2)
    
    data3 = data1[:,[0,2,3]]
    print(data3)
    
# test2()

def test3():
    data = np.random.randint(0,10,(10,5))
    print(data, data.shape)
    data1 = data[:, :3]
    print(data1)
    
    data = np.random.randint(0,14,(10,20))
    print(data,data.shape)
    data1 = data[:,-4:]
    print(data1)
    
# test3()

def test4():
    data = np.random.randint(10,20,(100,5))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data[:40,:]
    print(data1, data1.shape)
    print("-------------------------------------------------------")
    
    data2 = data[-20:,:]
    print(data2, data2.shape)
    
# test4()

def test5():
    data = np.random.randint(0,10,(10,))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data.reshape(2, 5)
    print(data1, data1.shape)
    print("-------------------------------------------------------")
    
    data = np.random.randint(10,20,(20,))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = data.reshape(5,-1)
    print(data1, data1.shape)

test5()