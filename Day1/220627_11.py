# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:23:33 2022

@author: Samsung
"""

import numpy as np
import matplotlib.pyplot as plt

def test1():
    data = np.random.randint(0,101,(100,5))
    print(data, data.shape)
    data1 = np.random.randint(0,101,(50,))
    
    x_data = data[:,0]
    y_data = data[:,-1]
    
    plt.plot(x_data,y_data, "r", label = "A Class")
    plt.grid()
    plt.legend()
    plt.show()

# test1()

def test2():
    data = np.random.randint(0,101,(50,3))
    print(data, data.shape)
    
    plt.plot(data[:,0],"b",label="score")
    plt.grid()
    plt.legend()
    plt.title("score")
    plt.show
    
    plt.plot(data[:,0],data[:,1], "rx",label="f01")
    plt.plot(data[:,0],data[:,2],"bo",label="f02")
    plt.show()
    
# test2()

def test3():
    data = np.random.randint(0,101,(100,3))
    print(data,data.shape)
    print("------------------------------------------------------------")
    
    plt.plot(data[:,0],"r",label="1 score")
    plt.plot(data[:,1],"g",label="2 score")
    plt.plot(data[:,2],"b",label="3 score")
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(data[:,0],data[:,1],"ro", label="1-2 score")
    plt.grid()
    plt.legend()
    plt.show()
    
test3()