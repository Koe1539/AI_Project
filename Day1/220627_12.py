# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:03:08 2022

@author: Samsung
"""

import numpy as np
import matplotlib.pyplot as plt

def test1():
    data1 = np.random.randint(0,11,(20,))
    print(data1, data1.shape)
    print("------------------------------------------------------------")
    
    data2 = np.random.rand(20,)
    print(data2, data2.shape)
    print("------------------------------------------------------------")
    
    plt.plot(data1)
    plt.plot(data2)
    plt.show()
    
    y1 = plt.axes()
    y1.plot(data1, "r")
    
    y2 = y1.twinx()
    y2.plot(data2, "b")
    
    plt.show()
    
# test1()

def test2():
    data1 = np.random.randint(0,101,(30,3))
    print(data1, data1.shape)
    print("-------------------------------------")
    
    data2 = np.random.rand(30,2)
    print(data2, data2.shape)
    
    a = plt.axes()
    a.plot(data1[:,0],"r",label="Kor")
    a.legend(loc="upper left")
    
    b = a.twinx()
    b.plot(data2[:,0],"b",label="data B")
    b.legend(loc="upper right")
    
    plt.grid()
    plt.show()

# test2()

def test3():
    data1 = np.random.randint(0,11,(10,))
    print(data1, data1.shape)
    
    data2 = np.random.randn(10,)
    print(data2, data2.shape)
    
    _,y1 = plt.subplots()
    y1.plot(data1,"r",label="data1")
    
    y2 = y1.twinx()
    y2.plot(data2,"b",label="data2")
    
    y1.legend(loc="upper left")
    y2.legend(loc="upper right")
    plt.show()

# test3()

def test4():
    data1 = np.random.randint(0,101,(30,))
    print(data1, data1.shape)
    print("-----------------------------------------")
    
    data2 = np.random.randint(0,101,(30,))
    print(data2, data2.shape)
    print("-----------------------------------------")
    
    plt.plot(data1,"r",label="A Class")
    plt.plot(data2,"b",label="B Class")
    
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.boxplot([data1,data2],labels=["A Class","B Class"])
    plt.show()    

test4()