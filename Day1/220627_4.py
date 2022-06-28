# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:16:34 2022

@author: Samsung
"""

import numpy as np

def test1():
    data = [2,5,6,7]
    print(type(data),data)
    data = np.array(data)
    print(type(data),data)
    print(data.shape)
    
    data1 = [[1,2],
             [1,3],
             [3,4]]
    
    data1 = np.array(data1)
    print(data1.shape)
    print(data1)

# test1()

def test2():
    data1 = np.random.randint(0,10,(10,))
    print(data1)
    data2 = np.random.randint(0,10,(2,3))
    print(data2)

# test2()

def test3():
    data1 = np.random.rand(5,3)
    print(data1)
    data2 = np.random.randn(5,3)
    print(data2)

# test3()
np.random.seed(2022)
def test4():
    data1 = np.random.randint(0,100,(30,3))
    for i in range(len(data1)):
        print(data1[i])
    # kor = data1[0][0]
    kor = data1[0,0]
    print(kor)

# test4()

def test5():
    data1 = np.random.randint(0,10,(3,4))
    data2 = np.random.randint(10,20,(3,4))
    print(data1.shape,data1)
    print(data2.shape,data2)
    a = data1 + data2
    b = data1 - data2
    c = data1 * data2
    d = data1 / data2
    print(a)
    print(b)
    print(c)
    print(d)
    e = data1 * 2
    print(e)

test5()





















