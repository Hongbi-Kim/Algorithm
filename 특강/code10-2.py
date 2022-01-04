# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:06:43 2022

@author: khb16
"""
# 재귀2
## 함수
def openBox():
    global count
    print("상자 열기")
    count -= 1
    if count == 0:
        print("** 반지를 넣고 반환합니다. **")
        return
    openBox()
    print("종이 상자를 닫습니다.")
    return

## 메인
count = 5
openBox() # 처음 함수를 다시 호출
# 상자 열기
# 상자 열기
# 상자 열기
# 상자 열기
# 상자 열기
# ** 반지를 넣고 반환합니다. **
# 종이 상자를 닫습니다.
# 종이 상자를 닫습니다.
# 종이 상자를 닫습니다.
# 종이 상자를 닫습니다.
