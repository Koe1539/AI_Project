# -*- coding: utf-8 -*-

import numpy as np
import cv2
from tensorflow.keras import datasets
from tensorflow.keras import models, layers
import random

# =============================================================================
# 모델 생성
# =============================================================================

def getData():
  (x_train, y_train), (x_test, y_test) = datasets.fashion_mnist.load_data()
  x_train = x_train.reshape(-1, 28 * 28)
  x_test = x_test.reshape(-1, 28 * 28)
  return (x_train, y_train), (x_test, y_test)

def makeModel():
  model = models.Sequential()
  model.add(layers.Dense(1000, activation='relu', input_shape=(28*28, )))
  model.add(layers.Dense(500, activation='relu'))
  model.add(layers.Dense(10, activation='softmax'))

  model.compile(loss = 'sparse_categorical_crossentropy',
                optimizer = 'adam', 
                metrics = ['accuracy'])
  print(model.summary())
  return model

def doRun():
  (x_train, y_train), (x_test, y_test) = getData()
  model = makeModel()

  log = model.fit(x_train, y_train, 
                  epochs = 2, batch_size = 16)
  model.save('fashion.h5')

  score = model.evaluate(x_test, y_test) # (문제, 답)
  print(score) # 최종 스코어

  lossH = log.history['loss']
  accH = log.history['accuracy']
  print(lossH, accH) # 지금까지 했던 epoch의 기록

# =============================================================================
# 생성된 모델을 바탕으로 테스트 및 결과값 도출
# img를 가져오는 것을 random 변수를 두어서 실행할 때 마다 랜덤으로 이미지를 추출하고 테스트하여 어떤 종류의 패션 아이템인지 맞춥니다.
# =============================================================================

def makeData():
  (x_train, y_train), (x_test, y_test) = datasets.fashion_mnist.load_data()
  img = x_test[random.randint(0, 10001)]
  cv2.imwrite('sample1.png', img)

def doPredict():
  x = cv2.imread('sample1.png', 0)
  x = x.reshape(-1, 28*28)

  model = models.load_model('fashion.h5')
  y_pre = model.predict(x)
  
  y_pre = np.argmax(y_pre)
  if y_pre == 0:
      print('티셔츠/상의')
  elif y_pre == 1:
      print('바지')
  elif y_pre == 2:
      print('스웨터/맨투맨')      
  elif y_pre == 3:
      print('드레스')
  elif y_pre == 4:
      print('코트')
  elif y_pre == 5:
      print('샌들')
  elif y_pre == 6:
      print('셔츠')  
  elif y_pre == 7:
      print('스니커즈')  
  elif y_pre == 8:
      print('가방')
  else:
      print('첼시부츠')      
      
makeData()
doPredict()
# doRun()

