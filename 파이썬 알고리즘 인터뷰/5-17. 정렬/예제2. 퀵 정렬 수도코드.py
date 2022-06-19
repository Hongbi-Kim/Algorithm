# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 23:50:27 2022

@author: khb16
"""

# 정렬
# 퀵 정렬 수도코드
def Quicksort(A, lo, hi):
    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)