# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:37:36 2022

@author: Samsung
"""
# 10~20사이의 숫자 중 7개를 선택 후 출력 
# 단, 중복이 없어야함.

import random

def test1():
    data = []
    while True:
        a = random.randint(10, 20)
        if a not in data:
            data.append(a)
        if len(data) == 7:
            break
        
    print(data)
# test1()

def test2():
    a = [1,3,5]
    b = [2,3,1]
    
    s = 0
    ball = 0
    
    for i in range(len(a)):
        if a[i]==b[i]:
            s = s + 1
            
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and i != j:
                ball = ball + 1
    print(a,b)
    print("s:",s)
    print("ball:",ball)
    
# test2()
def getinput():
    input_list = []
    while True:
        a = int(input())
        if a not in input_list:
            input_list.append(a)
        if len(input_list) == 3:
            break
    return input_list

def getdata():
    data = []
    while True:
        a = random.randint(0,9)
        if a not in data:
            data.append(a)
        if len(data) == 3:
            break
    return data

def getsb(data1,data2):
    s = 0
    b = 0
    
    for i in range(len(data1)):
        if data1[i]==data2[i]:
            s = s + 1
    
    for i in range(len(data1)):
        for j in range(len(data2)):
            if data1[i]==data2[j] and i != j:
                b = b + 1
                
    return s,b

def test3():
    data1 = getdata()
    data2 = getdata()
    
    s,b = getsb(data1,data2)
    
    print(data1,data2)
    print("s:",s)
    print("b:",b)

test3()