# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:06:49 2022

@author: Samsung
"""

import numpy as np
import matplotlib.pyplot as plt

def test1():
    data = np.random.randint(0,10,(2,3,4))
    print(data, data.shape)
    print("----------------------------------------------------------")
    
    data1 = data[0]
    print(data1, data1.shape)
    print("----------------------------------------------------------")
    
# test1()

def test2():
    data = np.random.randint(0,10,(10,))
    print(data, data.shape)
    print("----------------------------------------------------------")
    
    plt.plot(data,"r")
    plt.show()
    
# test2()

def test3():
    data1 = np.random.randint(0,101,(20,))
    data2 = np.random.randint(0, 101,(30,))
    
    plt.plot(data1, "g", label = "A반 성적")
    plt.plot(data2, "r", label = "B반 성적")
    plt.legend()
    plt.show()
    
# test3()

def test4():
    data1 = np.random.randint(0,101,(50,))
    data2 = np.random.randint(0,101,(50,))
    data3 = np.random.randint(0,101,(50,))
    
    plt.plot(data1,"r", label = "A Class")
    plt.plot(data2,"g", label = "B Class")
    plt.plot(data3,"b", label = "C Class")
    plt.legend()
    plt.show()
    
test4()