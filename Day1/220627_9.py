# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:27:45 2022

@author: Samsung
"""

"""
30명의 학생이 있다.
국영수 3개의 시험을 봤다.
학생 개인의 평균을 구하고 싶다.

총점
평균
"""

import numpy as np
np.random.seed(24)

def average():
    data = np.random.randint(0,101,(30,3))
    
    kor = data[:,0]
    eng = data[:,1]
    math = data[:,2]
    _sum = kor + eng + math
    ave = _sum // 3
    _sum = _sum.reshape(-1,1)
    ave = ave.reshape(-1,1)
    result = np.concatenate([data, _sum,ave], axis=1)
    print(result)
    
average()

def test1():
    data = np.random.randint(0,10,(5,2))
    print(data, data.shape)
    print("-------------------------------------------------------")
    
    data1 = np.random.randint(50,60,(5,3))
    print(data1, data1.shape)
    print("-------------------------------------------------------")
    
    data3 = np.concatenate([data,data1], axis=1)
    print(data3, data3.shape)
    
# test1()