# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 00:05:30 2022

@author: khb16
"""

# 7
# 럭키 스트레이트

data = input()
length = len(data) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(data[i])
    
# 오른쪽 부분의 자릿수 합 빼기    
for i in range(length // 2, length):
    summary -= int(data[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')
    
'''
123402
LUCKY
'''

# ------------------------------------------------------

# 8
# 문자열 재정렬


