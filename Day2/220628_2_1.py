# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:31:34 2022

@author: Samsung
"""

import cv2

def test1():
  img = cv2.imread("purple.png")
  print(img.shape)

  cv2.imshow("Purple",img)
  cv2.waitKey(0) # 입력을 무한정 기다림.
  cv2.destroyAllWindows()

# test1()

def test2():
    img = cv2.imread("purple.png")
    print(img.shape)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print(img1.shape)
    
    cv2.imshow("Gray_Purple",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("Gray_Purple.png",img1)
# test2()

def test3():
    img = cv2.imread("purple.png")
    print(img.shape)
    
    w,h,_ = img.shape
    print(w,h)
    
    w = int(w * 0.5)
    h = int(h * 0.5)
    print(w,h)
    
    img1 = cv2.resize(img, (w,h))
    print(img1.shape)
    
    cv2.imshow("Purple",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
# test3()

# =============================================================================
# 인터넷에서 이미지파알 하나 구할 것 -> color를 gray로 전환
# -> 이미지 크기를 절반으로 줄이기 -> 이미지 출력
# =============================================================================

def test4():
    img = cv2.imread("dog.jpg")
    cv2.imshow("Dog",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Gray_Dog",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    w,h,_ = img.shape
    w = int(w * 0.5)
    h = int(h * 0.5)
    img2 = cv2.resize(img,(w,h))
    cv2.imshow("Resize_Dog",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

test4()