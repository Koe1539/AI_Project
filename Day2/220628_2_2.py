# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:09:42 2022

@author: Samsung
"""

import numpy as np
import cv2

import numpy as np
import cv2

def test1() :
    img = cv2.imread("dog.jpg")
    print(img.shape)
    
    # cv2.imshow("Dog", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # HSV로 전환
    print(img2.shape)
    
    cv2.imshow("HSV_Dog", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# test1()

import os

def my_make_data():
    path = "./data"
    file_list = os.listdir(path)
    # print(file_list)
    
    data = []
    
    for i in range(len(file_list)):
        file_path = path + "/" + file_list[i]
        # print(file_path)
        
        img = cv2.imread(file_path,0)
        img = cv2.resize(img, (320,240))
        print(file_path, img.shape)
                
        data.append(img)
        
    data = np.array(data)
    print(data.shape)

my_make_data()