# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 23:47:09 2022

@author: khb16
"""

# 정렬
# 버블 정렬 수도코드
# 중요하진 않음. 정렬 자체가 실무와 다소 거리가 있음.

def Bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]