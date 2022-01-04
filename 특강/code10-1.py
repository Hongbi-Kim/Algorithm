# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:03:59 2022

@author: khb16
"""
# 재귀1
## 함수
def openBox():
    print("상자 열기")
    openBox()

## 메인
openBox() # 처음 함수를 다시 호출
