# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:34:05 2022

@author: khb16
"""

# 그리디
# 배낭문제
# 짐을 쪼갤 수 있을 때 -> 그리디
# 짐을 쪼갤 수 없을 때 -> 다이나믹 프로그래밍

cargo = [(4,12), (2,1),(10,4), (1,1), (2,2)] # (가격, 무게)

def fractional_knapsack(cargo):
    capacity = 15 # 최대 무게
    pack = []
    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse = True) # 단가 높은 순
    
    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            
    return total_value
    
fractional_knapsack(cargo)
# 17.333333333333332
