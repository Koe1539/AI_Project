# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:15:32 2022

@author: Samsung
"""

"""
비만도(BMI) = 몸무게(kg) / 키(m)**2
1) 1.83 86
2) 1.76 74
3) 1.69 59
4) 1.86 95
5) 1.77 80
6) 1.78 68
7) 1.78 60
"""

import numpy as np

def check_bmi():
    w = [86,74,59,95,80,68,60]
    h = [1.83, 1.76, 1.69, 1.86, 1.77, 1.78, 1.78]
    
    np_w = np.array(w)
    np_h = np.array(h)
    BMI = np_w / np_h ** 2
    data = np.where(BMI > 27, '비만','정상')
    return data
    
result = check_bmi()
print(result)